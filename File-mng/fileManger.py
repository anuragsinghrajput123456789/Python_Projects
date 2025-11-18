import os


def create_file(filename):
    try:
        with open(filename, "w") as f:
            print(f"File {filename} created")
    except Exception as e:
        print("Error", e)


def view_all_file():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("Files:")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error", e)


def read_file(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error", e)


def edit_file(filename):
    try:
        with open(filename, "a") as f:
            content = input("Enter text: ")
            f.write(content + "\n")
            print(f"Content added to {filename}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error", e)


def main():
    while True:
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            filename = input("Enter file name: ")
            create_file(filename)
        elif choice == "2":
            view_all_file()
        elif choice == "3":
            filename = input("Enter file name: ")
            delete_file(filename)
        elif choice == "4":
            filename = input("Enter file name: ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter file name: ")
            edit_file(filename)
        elif choice == "6":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
