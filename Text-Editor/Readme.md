🧠 Mini IDE Ultimate v4 🚀

A lightweight, AI-powered, multi-tab code editor built in pure Python + Tkinter — featuring AI Autocomplete (Gemini), syntax highlighting, run console, themes, autosave, and more!

📸 Preview

(Add screenshots here)

[Add Screenshot: Main Editor]
[Add Screenshot: Run Console + Dark Mode]
[Add Screenshot: Theme Palette]

✨ Features
Category Description
🧩 Multi-Tab Editing Open, edit, and manage multiple files at once
🧠 AI Autocomplete Powered by Gemini API — auto-continue text/code with Ctrl + Space
💡 Syntax Highlighting Supports Python, JavaScript, HTML, CSS, and JSON
💾 Auto-Save System Automatically saves every 60s (configurable)
🌈 Theme Palette Choose from 5 beautiful themes (Dracula, Monokai, Solarized, etc.) or pick your own custom color
⚙️ Persistent Theme Your theme is saved locally for next run
▶️ Run Console Execute .py files directly inside the IDE (outputs in bottom console)
🔍 Search & Replace Quick text find and replace bar
🖱️ Zoom In/Out Use Ctrl + MouseWheel to adjust font size dynamically
💬 Shortcut Helper Panel Quick reference guide built into the app
🌗 Dark / Light Mode Toggle instantly between dark and light schemes
🪄 Smooth Animations & Transitions Built using Tkinter’s elegant event system
🛟 Cross-Platform Works on Windows, macOS, and Linux
🧰 Tech Stack

🐍 Python 3.9+

🧱 Tkinter (UI)

💬 Requests (for Gemini AI API calls)

🔑 python-dotenv (to store your API key)

🧩 Subprocess (to run .py files in console)

⚙️ Installation
1️⃣ Clone this Repository
git clone https://github.com/yourusername/mini-ide-ultimate.git
cd mini-ide-ultimate

2️⃣ Install Dependencies
pip install requests python-dotenv

3️⃣ Add Your Gemini API Key

Create a file named .env in the project folder:

GEMINI_API_KEY=your_api_key_here

You can get a free Gemini API key from:
👉 https://aistudio.google.com/app/apikey

🏃 Usage
Start the IDE
python mini_ide_v4.py

Once Opened:

🧩 Create / Open Files

Ctrl + N → New tab

Ctrl + O → Open file

Ctrl + S → Save

🧠 AI Assist

Ctrl + Space → Generate AI completion (code/text continuation)

▶️ Run Python Files

F5 → Run .py file (output appears in bottom console)

🎨 Themes

View → Theme Palette → Pick theme

🎨 Choose from Default, Monokai, Dracula, Solarized, Light

💾 Theme is saved persistently in theme.cfg

🔍 Find & Replace

Ctrl + F → Toggle find/replace bar in the current tab

🖱️ Zoom

Ctrl + MouseWheel → Zoom in/out text

🌗 Dark/Light Toggle

Click 🌗 button or via menu → “View → Toggle Theme”

💾 Auto-Save

Enabled by default (every 60 seconds)

Temporary autosaves stored safely in system temp folder

🧠 Shortcut Reference
Action Shortcut
🆕 New Tab Ctrl + N
📂 Open File Ctrl + O
💾 Save File Ctrl + S
🧠 AI Complete Ctrl + Space
🔍 Find / Replace Ctrl + F
▶️ Run Python F5
🔍 Zoom Ctrl + MouseWheel
🌗 Toggle Theme via Menu or Theme Button
🪟 Theme Palette View → Theme Palette
🛟 Auto-Save Every 60s (configurable)
🧩 Folder Structure
📂 mini-ide-ultimate/
│
├── mini_ide_v4.py # Main application
├── .env # Gemini API key
├── theme.cfg # Stores last selected theme
├── README.md # Documentation
└── requirements.txt # Dependencies (optional)

🧪 Screenshots (Suggested)

You can add these later in your README:

🖥️ Default Editor Layout

🧠 AI Suggestion Example

🎨 Theme Palette (Dracula, Solarized, etc.)

▶️ Run Console Output

🛠️ Customization
🎨 Change Auto-Save Interval

Go to:
View → Auto-save Interval
Set custom time (in seconds).

🌈 Add New Theme

Add new theme JSON inside THEMES dictionary in code:

"Ocean": {"bg":"#001F3F","fg":"#7FDBFF","accent":"#39CCCC"}

🧠 Disable AI (Offline Mode)

Remove or comment out AI key:

# GEMINI_API_KEY=

🧡 Credits

Created by [Your Name] ✨
Built with 💻 Python & Tkinter
Inspired by VS Code, powered by Gemini AI 🧠

📜 License

This project is open-source under the MIT License — you’re free to modify and distribute.

💬 Future Plans

🚧 Coming soon:

🪶 Built-in Code Formatter (Black/Prettier)

🪟 Split Editor (side-by-side file editing)

🧩 Plugin Support

🧠 Gemini Chat Panel (inline code explanation)

🏁 Final Thoughts

Mini IDE Ultimate v4 proves that you can build a powerful, modern, and AI-assisted IDE —
all in Python’s Tkinter, with zero external UI libraries 💪

“It’s like VS Code, built from scratch — by you!” ⚡
