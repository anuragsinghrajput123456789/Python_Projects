from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set in .env file")


# Connect DB function is being intialized here...
def connectDB(uri):
    try:
        client = MongoClient(uri)
        print("✅ Connected to MongoDB successfully")
        return client
    except Exception as e:
        print("❌ Error connecting to MongoDB:", e)
        sys.exit(1)


# Connect to DB
client = connectDB(MONGO_URI)
db = client["ytmanager"]
video_collection = db["videos"]
print(video_collection)


def list_videos():
    videos = video_collection.find()
    for video in videos:
        print(
            f"ID: {video['_id']}, Name: {video.get('name')}, and Time: {video.get('time')}"
        )


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(video_ID, name, time):
    try:
        video_collection.update_one(
            {"_id": ObjectId(video_ID)},
            {"$set": {"name": name, "time": time}},
        )
        print("✅ Video updated successfully")
    except Exception as e:
        print("❌ Error updating video:", e)


def delete_video(video_ID):
    try:
        video_collection.delete_one({"_id": ObjectId(video_ID)})
        print("🗑️ Video deleted successfully")
    except Exception as e:
        print("❌ Error deleting video:", e)


def main():
    while True:
        print("\n YouTube Manager App")
        print("---------------------- * ---------------------")
        print("1. List Videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice : ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name, time)
        elif choice == "3":
            video_ID = input("Enter the video id to update : ")
            name = input("Enter the new name : ")
            time = input("Enter the new time : ")
            update_video(video_ID, name, time)
        elif choice == "4":
            video_ID = input("Enter the video id to delete : ")
            delete_video(video_ID)
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
