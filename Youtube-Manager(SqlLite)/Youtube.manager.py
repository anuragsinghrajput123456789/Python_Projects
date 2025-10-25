import sqlite3

# Connect to the database (it will create the file if it doesn't exist)
conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

# Create table
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS videos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);
"""
)
conn.commit()


def list_videos():
    cursor.execute("SELECT * FROM videos")
    if videos := cursor.fetchall():
        for row in videos:
            print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")

    else:
        print("No videos found.")


def add_video(name, time):
    name = name.strip()
    time = time.strip()
    if not name or not time:
        print("❌ Name and time cannot be empty!")
        return
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("✅ Video added successfully!")


def update_video(video_id, name, time):
    try:
        video_id = int(video_id)
    except ValueError:
        print("❌ Invalid ID. Must be a number.")
        return
    cursor.execute("SELECT * FROM videos WHERE ID = ?", (video_id,))
    if cursor.fetchone() is None:
        print("❌ No video found with that ID.")
        return
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE ID = ?",
        (name.strip(), time.strip(), video_id),
    )
    conn.commit()
    print("✅ Video updated successfully!")


def delete_video(video_id):
    try:
        video_id = int(video_id)
    except ValueError:
        print("❌ Invalid ID. Must be a number.")
        return
    cursor.execute("SELECT * FROM videos WHERE ID = ?", (video_id,))
    if cursor.fetchone() is None:
        print("❌ No video found with that ID.")
        return
    cursor.execute("DELETE FROM videos WHERE ID = ?", (video_id,))
    conn.commit()
    print("✅ Video deleted successfully!")


def main():
    while True:
        print("\n=== YouTube Video Manager (SQLite) ===")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("👋 Exiting application.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
