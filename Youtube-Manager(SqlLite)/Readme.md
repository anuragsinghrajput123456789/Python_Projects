YouTube Video Manager (SQLite)

A simple command-line application to manage your YouTube video collection using Python and SQLite. You can list, add, update, and delete videos with ease.

Features

✅ List Videos – View all videos with ID, name, and duration.

✅ Add Video – Store a new video with its name and duration.

✅ Update Video – Update the name and duration of an existing video.

✅ Delete Video – Remove a video by its ID.

✅ Input Validation – Ensures IDs are numeric and fields are not empty.

✅ Persistent Storage – Uses SQLite database (youtube_videos.db).

Requirements

Python 3.x

SQLite (comes pre-installed with Python)

No external libraries are required.

Installation



Run the application:

python youtube_video_manager.py

Usage

When you run the program, a menu will appear:

=== YouTube Video Manager (SQLite) ===
1. List Videos
2. Add Video
3. Update Video
4. Delete Video
5. Exit

1. List Videos

Displays all saved videos with their ID, name, and duration.

2. Add Video

Prompts for the video name and duration:

Enter the video name: Python Tutorial
Enter the video duration: 10:30
✅ Video added successfully!

3. Update Video

Update a video by ID:

Enter the video ID to update: 1
Enter the new video name: Advanced Python Tutorial
Enter the new video time: 15:45
✅ Video updated successfully!

4. Delete Video

Delete a video by ID:

Enter the video ID to delete: 1
✅ Video deleted successfully!

5. Exit

Exits the program safely.

Database

File: youtube_videos.db

Table: videos

Columns:

ID (INTEGER, PRIMARY KEY, AUTOINCREMENT)

name (TEXT, NOT NULL)

time (TEXT, NOT NULL)

The database file will be automatically created in the same folder when running the program for the first time.

Notes

Ensure duration is in MM:SS or HH:MM:SS format (e.g., 10:30 or 1:02:15).

Video IDs must be numeric when updating or deleting.

License

This project is open-source and free to use.