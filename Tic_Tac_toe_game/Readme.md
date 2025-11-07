🧠 Tic Tac Toe AI (Tkinter + Pandas)

A modern Tic Tac Toe Game built with Python Tkinter, featuring:

🧠 Smart AI opponent

👥 Player vs Player (PVP) mode

📊 Live scoreboard

💾 Score persistence using Excel (via Pandas)

🎨 Clean UI with animations and colors

🖼️ Preview
Game Window	Scoreboard

	
✨ Features

✅ Two Modes:

👤 Player vs AI (Computer)

👥 Player vs Player (Local)

✅ Smart AI Logic:

Blocks your winning moves 🧩

Plays random or strategic moves intelligently

✅ Beautiful UI:

Clean modern theme

Colored highlights for wins

Smooth buttons & clear text indicators

✅ Scoreboard System:

Tracks Wins, Losses, and Draws live

Displays total games

Stores results in an Excel sheet (tictactoe_scores.xlsx)

✅ Persistence:

When you reopen the game, scores are automatically loaded from Excel 📂

✅ Control Buttons:

🔁 Restart Match (keeps scores)

🧹 Reset Scores (clears Excel + live scoreboard)

🧩 Tech Stack
Component	Description
Language	Python 3.8+
GUI Library	Tkinter
Data Handling	Pandas
File Storage	Excel (.xlsx) using openpyxl
Platform	Works on Windows / macOS / Linux
⚙️ Installation & Setup

Clone this repository

git clone https://github.com/<your-username>/TicTacToe-AI.git
cd TicTacToe-AI


Install dependencies

pip install pandas openpyxl


Run the game

python tictactoe_ai.py


Enjoy 🎮

📊 Excel Score Tracking

All match results are saved in tictactoe_scores.xlsx in the project folder.

Player	Opponent	Result	Winner
You	Computer	You Won	X
Player X	Player O	Draw	Draw
You	Computer	Computer Won	O
🕹️ Controls
Action	Description
Click on cells	Place your move (X or O)
Restart 🔁	Starts a new match, keeps scores
Reset Scores 🧹	Clears Excel file & live scores
Mode Switch	Choose AI or PVP before starting
💡 Future Enhancements

🚀 Planned upgrades:

🤖 Unbeatable AI using Minimax algorithm

🎚️ Difficulty Levels (Easy / Hard)

🔊 Sound effects for clicks & wins

🌗 Dark/Light theme toggle

🧾 Export scoreboard to PDF

🧑‍💻 Author

Anurag Singh
💻 MERN Stack | Machine Learning | Python Dev
🌐 LinkedIn
 | GitHub
 | Twitter

🪪 License

This project is licensed under the MIT License — feel free to use and modify it.

⭐ Show Some Love

If you like this project:

🌟 Star it on GitHub

💬 Share feedback or ideas

🧩 Contribute by improving AI or UI