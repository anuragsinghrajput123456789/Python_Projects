🎬 YouTube Manager CLI (Python)

A simple command-line app to manage your favorite YouTube videos — add, update, delete, and list them easily!
Data is saved locally in a .json or .txt file using Python’s built-in JSON module.

🚀 Features

📄 List All Videos — View all your saved YouTube videos in a clean formatted list

➕ Add Video — Add new videos with name and duration

✏️ Update Video — Edit existing video details

🗑️ Delete Video — Remove videos by index

💾 Choose File Type — Save data as either .json or .txt

⚡ Auto-Save — All changes are instantly saved

🧱 Error-Handled — Fully protected from invalid inputs and file issues

🧰 Tech Stack

Language: Python 3.x

Libraries:

json (for serialization)

os (for file handling)

📦 Installation & Setup

Clone or download this repository

git clone https://github.com/anuragsinghrajput123456789/Python_Projects/settings
cd youtube-manager-cli


Run the program

python main.py


On first run, you’ll be asked:

Choose file type to store data:
1. JSON file (Recommended)
2. TXT file


→ Choose your preferred option and start managing your videos!

🧭 Usage Guide
Option	Description
1	List all YouTube videos
2	Add a new YouTube video
3	Update existing video details
4	Delete a YouTube video
5	Exit the application

Example interaction:

📺 Your Personal YouTube Manager
========================================
1️⃣  List All YouTube Videos
2️⃣  Add a YouTube Video
3️⃣  Update a YouTube Video
4️⃣  Delete a YouTube Video
5️⃣  Exit the Application
========================================
Enter your choice: 2
Enter video name: Python Basics
Enter video duration: 15min
✅ Data saved successfully!

🗂️ Data Storage

Your data is stored in the same directory as:

youtube.json (default, recommended)
or

youtube.txt (optional)

Both files store structured JSON data, e.g.:

[
  {"name": "Python Basics", "time": "15min"},
  {"name": "DSA Crash Course", "time": "25min"}
]

⚙️ Error Handling

Prevents crashes from invalid input

Handles missing or corrupted files gracefully

Uses .get() to avoid missing-key errors

💡 Future Enhancements

Add video search/filter feature

Export list to CSV or Excel

Add a GUI version using Tkinter or PyQt

Integrate with YouTube API to fetch metadata automatically

🧑‍💻 Author

Anurag Singh
💼 100 Days of DSA & Projects Challenge
📧 Reach out for feedback or suggestions!
