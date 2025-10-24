import json
import os


def choose_file_type():
    """Ask user which file type to use (json/txt)."""
    while True:
        print("\nChoose file type to store data:")
        print("1. JSON file (Recommended)")
        print("2. TXT file")
        choice = input("Enter your choice (1/2): ")
        if choice == "1":
            return "youtube.json"
        elif choice == "2":
            return "youtube.txt"
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")


def load_data(filename):
    """Load video data safely from chosen file type."""
    try:
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("⚠️ File is empty or corrupted, starting fresh.")
        return []
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return []


def save_data_helper(videos, filename):
    """Save all video data safely."""
    try:
        with open(filename, "w") as file:
            json.dump(videos, file, indent=4)
        print("✅ Data saved successfully!")
    except Exception as e:
        print(f"❌ Error saving data: {e}")


def list_all_videos(videos):
    """Pretty-print the list of videos."""
    print("\n" + "=" * 70)
    print("🎬 Your YouTube Videos".center(70))
    print("=" * 70)

    if not videos:
        print("⚠️ No videos found! Add some first.")
    else:
        for index, video in enumerate(videos, start=1):
            name = video.get("name", "N/A")
            time = video.get("time", "N/A")
            print(f"{index:>2}. 🎥 Title: {name:<25} | ⏱ Duration: {time}")

    print("=" * 70 + "\n")


def add_video(videos, filename):
    """Add a new video with error handling."""
    try:
        name = input("Enter video name: ").strip()
        time = input("Enter video duration: ").strip()

        if not name or not time:
            print("⚠️ Both name and duration are required!")
            return

        videos.append({"name": name, "time": time})
        save_data_helper(videos, filename)
    except Exception as e:
        print(f"❌ Error adding video: {e}")


def update_video(videos, filename):
    """Update details of an existing video."""
    try:
        if not videos:
            print("⚠️ No videos to update.")
            return

        list_all_videos(videos)
        index = int(input("Enter the video number to update: "))

        if 1 <= index <= len(videos):
            name = input("Enter new video name: ").strip()
            time = input("Enter new video duration: ").strip()
            if name:
                videos[index - 1]["name"] = name
            if time:
                videos[index - 1]["time"] = time
            save_data_helper(videos, filename)
        else:
            print("❌ Invalid video number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")
    except Exception as e:
        print(f"❌ Error updating video: {e}")


def delete_video(videos, filename):
    """Delete a video by index."""
    try:
        if not videos:
            print("⚠️ No videos to delete.")
            return

        list_all_videos(videos)
        index = int(input("Enter the video number to delete: "))

        if 1 <= index <= len(videos):
            removed = videos.pop(index - 1)
            print(f"🗑 Deleted: {removed.get('name', 'Unknown')}")
            save_data_helper(videos, filename)
        else:
            print("❌ Invalid video number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")
    except Exception as e:
        print(f"❌ Error deleting video: {e}")


def main():
    filename = choose_file_type()
    videos = load_data(filename)

    while True:
        print("\n📺 Your Personal YouTube Manager")
        print("=" * 40)
        print("1️⃣  List All YouTube Videos")
        print("2️⃣  Add a YouTube Video")
        print("3️⃣  Update a YouTube Video")
        print("4️⃣  Delete a YouTube Video")
        print("5️⃣  Exit the Application")
        print("*" * 40)

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos, filename)
            case "3":
                update_video(videos, filename)
            case "4":
                delete_video(videos, filename)
            case "5":
                print("👋 Exiting the application... Goodbye!")
                break
            case _:
                print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
