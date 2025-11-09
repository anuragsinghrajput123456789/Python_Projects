import os, re, time, tempfile, requests, tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# ------------------------------------------
# 🔍 Syntax Patterns (same as before)
# ------------------------------------------
EXT_LANG = {
    ".py": "python",
    ".js": "javascript",
    ".json": "json",
    ".html": "html",
    ".htm": "html",
    ".css": "css",
}
PY_KW = r"\b(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b"
PATTERNS = {
    "python": [
        ("kw", PY_KW, 0),
        ("com", r"#.*?$", re.M),
        ("str", r"(['\"])(?:(?=(\\?))\2.)*?\1", 0),
        ("num", r"\b\d+(\.\d+)?\b", 0),
    ]
}


# ==========================================
# 🧠 Mini IDE Class
# ==========================================
class MiniIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini IDE Ultimate v3 ✨")
        self.root.geometry("1200x720")
        self.dark = False
        self.autosave_interval = 60000
        self.autosave_enabled = True
        self._debounce = None

        # -------- Menu Bar --------
        menubar = tk.Menu(root)
        filem = tk.Menu(menubar, tearoff=0)
        filem.add_command(
            label="🆕 New Tab", command=self.new_tab, accelerator="Ctrl+N"
        )
        filem.add_command(label="📂 Open", command=self.open_file, accelerator="Ctrl+O")
        filem.add_command(label="💾 Save", command=self.save_file, accelerator="Ctrl+S")
        filem.add_separator()
        filem.add_command(label="🪄 Close Tab", command=self.close_tab)
        filem.add_command(label="❌ Close All", command=self.close_all)
        filem.add_command(label="🚪 Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filem)

        editm = tk.Menu(menubar, tearoff=0)
        editm.add_command(
            label="Find / Replace", command=self.toggle_search, accelerator="Ctrl+F"
        )
        menubar.add_cascade(label="Edit", menu=editm)

        viewm = tk.Menu(menubar, tearoff=0)
        viewm.add_command(label="🌗 Toggle Theme", command=self.toggle_theme)
        viewm.add_command(label="⚙️ Auto-save Interval", command=self.change_interval)
        menubar.add_cascade(label="View", menu=viewm)

        aim = tk.Menu(menubar, tearoff=0)
        aim.add_command(
            label="✨ AI Autocomplete",
            command=self.ai_complete,
            accelerator="Ctrl+Space",
        )
        menubar.add_cascade(label="AI", menu=aim)
        root.config(menu=menubar)

        # -------- Layout Frames --------
        container = ttk.Frame(root)
        container.pack(fill="both", expand=True)
        self.notebook = ttk.Notebook(container)
        self.notebook.pack(side="left", fill="both", expand=True, padx=3, pady=3)

        # Shortcut helper side panel
        self.helper = tk.Text(
            container,
            width=30,
            wrap="word",
            state="disabled",
            bg="#fafafa",
            fg="#333",
            font=("Segoe UI", 10),
        )
        self.helper.pack(side="right", fill="y")
        self._populate_shortcuts()

        # Status bar
        self.status = tk.Label(root, text="Ready", anchor="w", bg="#f0f0f0")
        self.status.pack(side="bottom", fill="x")

        # First tab
        self.new_tab()

        # Shortcuts
        root.bind("<Control-n>", lambda e: self.new_tab())
        root.bind("<Control-o>", lambda e: self.open_file())
        root.bind("<Control-s>", lambda e: self.save_file())
        root.bind("<Control-f>", lambda e: self.toggle_search())
        root.bind("<Control-space>", lambda e: self.ai_complete())

        self._schedule_autosave()

    # ======================================
    # 📄 Tab Management
    # ======================================
    def new_tab(self):
        frame = ttk.Frame(self.notebook)
        search = tk.Frame(frame, bg="#f0f0f0")
        find_e = tk.Entry(search, width=20)
        repl_e = tk.Entry(search, width=20)
        tk.Label(search, text="Find:", bg="#f0f0f0").pack(side="left")
        find_e.pack(side="left")
        tk.Label(search, text=" Replace:", bg="#f0f0f0").pack(side="left")
        repl_e.pack(side="left")
        ttk.Button(
            search, text="Find", command=lambda: self.find_text(t, find_e.get())
        ).pack(side="left")
        ttk.Button(
            search,
            text="Replace",
            command=lambda: self.replace_text(t, find_e.get(), repl_e.get()),
        ).pack(side="left")
        search.pack_forget()

        t = tk.Text(frame, wrap="word", font=("Consolas", 13), undo=True)
        t.pack(fill="both", expand=True, padx=3, pady=3)
        t.bind("<<Modified>>", self._on_modified)
        t.bind("<KeyRelease>", self._debounced_highlight)

        frame.text, frame.search, frame.find_e, frame.repl_e = t, search, find_e, repl_e
        frame.path, frame.lang, frame.dirty = None, "plain", False
        self._init_tags(t)
        self.notebook.add(frame, text="Untitled ×")
        self.notebook.select(frame)
        self._apply_theme(frame)

    def current_tab(self):
        tab = self.notebook.select()
        return self.notebook.nametowidget(tab) if tab else None

    def close_tab(self):
        tab = self.current_tab()
        if tab:
            self.notebook.forget(tab)

    def close_all(self):
        for t in self.notebook.winfo_children():
            self.notebook.forget(t)
        self.new_tab()

    # ======================================
    # 🔍 Search / Replace
    # ======================================
    def toggle_search(self):
        tab = self.current_tab()
        if not tab:
            return
        sb = tab.search
        sb.pack_forget() if sb.winfo_ismapped() else sb.pack(side="top", fill="x")

    def find_text(self, tw, q):
        tw.tag_remove("found", "1.0", tk.END)
        if not q:
            return
        pos = "1.0"
        while True:
            p = tw.search(q, pos, stopindex=tk.END, nocase=1)
            if not p:
                break
            e = f"{p}+{len(q)}c"
            tw.tag_add("found", p, e)
            pos = e
        tw.tag_config("found", background="#0078d7", foreground="white")

    def replace_text(self, tw, f, r):
        if not f:
            return
        c = tw.search(f, "1.0", stopindex=tk.END)
        if c:
            e = f"{c}+{len(f)}c"
            tw.delete(c, e)
            tw.insert(c, r)
            self.find_text(tw, f)

    # ======================================
    # 📂 File Operations
    # ======================================
    def open_file(self):
        p = filedialog.askopenfilename(filetypes=[("All", "*.*")])
        if not p:
            return
        t = self.current_tab()
        t.text.delete("1.0", tk.END)
        with open(p, "r", encoding="utf-8") as f:
            t.text.insert("1.0", f.read())
        t.path = p
        t.lang = self._lang(p)
        t.dirty = False
        self.notebook.tab(t, text=os.path.basename(p) + " ×")
        self._highlight_now(t)

    def save_file(self):
        t = self.current_tab()
        if not t:
            return
        if not t.path:
            p = filedialog.asksaveasfilename(defaultextension=".txt")
            if not p:
                return
            t.path = p
            t.lang = self._lang(p)
        with open(t.path, "w", encoding="utf-8") as f:
            f.write(t.text.get("1.0", tk.END))
        t.dirty = False
        self.notebook.tab(t, text=os.path.basename(t.path) + " ×")
        self.status.config(text=f"Saved {t.path}")

    # ======================================
    # 🧠 AI Autocomplete
    # ======================================
    def ai_complete(self):
        t = self.current_tab()
        if not (t and GEMINI_API_KEY):
            messagebox.showinfo("AI", "Add GEMINI_API_KEY in .env")
            return
        ctx = t.text.get("1.0", tk.INSERT)[-2000:]
        if not ctx:
            return
        self.status.config(text="AI thinking…")
        try:
            r = requests.post(
                "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
                headers={
                    "x-goog-api-key": GEMINI_API_KEY,
                    "Content-Type": "application/json",
                },
                json={"contents": [{"parts": [{"text": "Continue:\n" + ctx}]}]},
                timeout=15,
            )
            txt = (
                r.json()
                .get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "")
            )
            if txt:
                t.text.insert(tk.INSERT, txt)
                t.dirty = True
                self.status.config(text="✨ AI completed")
        except Exception as e:
            self.status.config(text=f"AI error: {e}")

    # ======================================
    # 💾 Auto-save
    # ======================================
    def _schedule_autosave(self):
        if self.autosave_enabled:
            for tab in self.notebook.winfo_children():
                if getattr(tab, "dirty", False):
                    p = tab.path or os.path.join(tempfile.gettempdir(), "autosave.txt")
                    open(p, "w", encoding="utf-8").write(tab.text.get("1.0", tk.END))
                    tab.dirty = False
                    self.status.config(text=f"Auto-saved {os.path.basename(p)}")
        self.root.after(self.autosave_interval, self._schedule_autosave)

    def change_interval(self):
        val = simpledialog.askinteger(
            "Auto-save", "Interval (seconds):", minvalue=5, maxvalue=600
        )
        if val:
            self.autosave_interval = val * 1000
            self.status.config(text=f"Auto-save={val}s")

    # ======================================
    # 🎨 Theme + Highlighting
    # ======================================
    def toggle_theme(self):
        self.dark = not self.dark
        for t in self.notebook.winfo_children():
            self._apply_theme(t)
        c1, c2 = ("#1e1e1e", "#9cdcfe") if self.dark else ("#f0f0f0", "black")
        self.status.config(bg=c1, fg=c2)

    def _apply_theme(self, tab):
        tw = tab.text
        if self.dark:
            tw.config(bg="#1e1e1e", fg="#d4d4d4", insertbackground="white")
        else:
            tw.config(bg="white", fg="black", insertbackground="black")

    def _init_tags(self, t):
        for n in ["kw", "str", "num", "com", "found"]:
            t.tag_config(
                n,
                foreground={
                    "kw": "#c586c0",
                    "str": "#ce9178",
                    "num": "#b5cea8",
                    "com": "#6a9955",
                    "found": "white",
                }.get(n),
            )
        t.tag_config("found", background="#0078d7")

    def _debounced_highlight(self, e):
        if self._debounce:
            self.root.after_cancel(self._debounce)
        self._debounce = self.root.after(200, self.highlight_current)

    def highlight_current(self):
        t = self.current_tab()
        if t:
            self._highlight_now(t)

    def _highlight_now(self, t):
        src = t.text.get("1.0", tk.END)
        for n in ["kw", "str", "num", "com"]:
            t.text.tag_remove(n, "1.0", tk.END)
        if t.lang != "python":
            return
        for tag, pat, flg in PATTERNS["python"]:
            for m in re.finditer(pat, src, flg):
                i = self._idx(src, m.start())
                e = self._idx(src, m.end())
                t.text.tag_add(tag, i, e)

    def _idx(self, s, o):
        line = s.count("\n", 0, o) + 1
        col = o - (s.rfind("\n", 0, o) + 1 if "\n" in s[:o] else 0)
        return f"{line}.{col}"

    def _lang(self, p):
        return EXT_LANG.get(os.path.splitext(p)[1].lower(), "plain")

    # ======================================
    # 🧾 Misc
    # ======================================
    def _on_modified(self, e):
        w = e.widget
        w.edit_modified(False)
        t = self.current_tab()
        if not t:
            return
        t.dirty = True
        lbl = os.path.basename(t.path) if t.path else "Untitled"
        self.notebook.tab(t, text=lbl + " *×")

    def _populate_shortcuts(self):
        tips = (
            "💡 Keyboard Shortcuts:\n"
            "Ctrl + N  → New Tab\n"
            "Ctrl + O  → Open File\n"
            "Ctrl + S  → Save\n"
            "Ctrl + F  → Find / Replace\n"
            "Ctrl + Space → AI Autocomplete\n"
            "Ctrl + MouseWheel → Zoom\n"
            "🌗 Button → Dark/Light Mode\n"
            "🛟 Auto-save → every set interval"
        )
        self.helper.config(state="normal")
        self.helper.delete("1.0", tk.END)
        self.helper.insert("1.0", tips)
        self.helper.config(state="disabled")


# ======================================
# 🚀 Run
# ======================================
if __name__ == "__main__":
    root = tk.Tk()
    MiniIDE(root)
    root.mainloop()
