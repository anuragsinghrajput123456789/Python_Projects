import tkinter as tk
from time import strftime
import datetime
import itertools

# ------------------------------
# 🕒 Create main window
# ------------------------------
root = tk.Tk()
root.title("Digital Clock by Anurag Singh ❤️")
root.geometry("600x350")
root.resizable(False, False)

# ------------------------------
# 🌈 Gradient Background Animation
# ------------------------------
colors = itertools.cycle(
    [
        "#0A0A0A",
        "#1B1B2F",
        "#16213E",
        "#0F3460",
        "#533483",
        "#2C2C54",
        "#3A0CA3",
        "#7209B7",
    ]
)


def animate_bg():
    next_color = next(colors)
    root.configure(bg=next_color)
    clock_label.configure(bg=next_color)
    date_label.configure(bg=next_color)
    month_label.configure(bg=next_color)
    credit_label.configure(bg=next_color)
    toggle_button.configure(bg=next_color)
    root.after(2500, animate_bg)  # change every 2.5 seconds


# ------------------------------
# 🌙 Light / Dark Mode Toggle
# ------------------------------
is_dark = True


def toggle_theme():
    global is_dark
    if is_dark:
        # Switch to Light Mode
        root.configure(bg="#F7F7F7")
        clock_label.configure(bg="#F7F7F7", fg="#000000")
        date_label.configure(bg="#F7F7F7", fg="#333333")
        month_label.configure(bg="#F7F7F7", fg="#555555")
        credit_label.configure(bg="#F7F7F7", fg="#444444")
        toggle_button.configure(
            text="🌙 Dark Mode", bg="#F7F7F7", fg="#000000", relief="groove"
        )
        is_dark = False
    else:
        # Switch to Dark Mode
        root.configure(bg="#0A0A0A")
        clock_label.configure(bg="#0A0A0A", fg="#00FFAB")
        date_label.configure(bg="#0A0A0A", fg="#FFFFFF")
        month_label.configure(bg="#0A0A0A", fg="#999999")
        credit_label.configure(bg="#0A0A0A", fg="#888888")
        toggle_button.configure(
            text="☀️ Light Mode", bg="#0A0A0A", fg="#00FFAB", relief="groove"
        )
        is_dark = True


# ------------------------------
# ⏰ Time and Date Function
# ------------------------------
def time():
    current_time = strftime("%H:%M:%S %p")
    today = datetime.date.today()
    day_name = today.strftime("%A")
    date_str = today.strftime("%d %B %Y")
    month_name = today.strftime("%B")

    clock_label.config(text=current_time)
    date_label.config(text=f"{day_name}, {date_str}")
    month_label.config(text=f"Month: {month_name}")
    clock_label.after(1000, time)


# ------------------------------
# 🎨 UI Components
# ------------------------------
clock_label = tk.Label(
    root,
    font=("Orbitron", 60, "bold"),
    background="#0A0A0A",
    foreground="#00FFAB",
    pady=10,
)
clock_label.pack(anchor="center", pady=(30, 10))

date_label = tk.Label(
    root, font=("Helvetica", 20, "bold"), background="#0A0A0A", foreground="#FFFFFF"
)
date_label.pack(anchor="center")

month_label = tk.Label(
    root, font=("Helvetica", 16), background="#0A0A0A", foreground="#999999"
)
month_label.pack(anchor="center")

# Theme toggle button
toggle_button = tk.Button(
    root,
    text="☀️ Light Mode",
    command=toggle_theme,
    bg="#0A0A0A",
    fg="#00FFAB",
    font=("Arial", 12, "bold"),
    relief="groove",
    activebackground="#111111",
    activeforeground="#00FFAB",
)
toggle_button.pack(anchor="center", pady=20)

# Footer credit
credit_label = tk.Label(
    root,
    text="Made with ❤️ by Anurag Singh",
    font=("Arial", 10, "italic"),
    background="#0A0A0A",
    foreground="#888888",
)
credit_label.pack(side="bottom", pady=10)

# ------------------------------
# 🚀 Start the clock and animations
# ------------------------------
time()
animate_bg()
root.mainloop()
