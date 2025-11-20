contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter name: ")
        if name in contacts:
            print(f"Contact {name} already exists")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")

            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
            print(f"Contact {name} created")

    elif choice == "2":
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(
                f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}"
            )
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter contact name to update: ")
        if name in contacts:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")

            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
            print(f"Contact {name} updated")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted")
        else:
            print("Contact not found")

    elif choice == "5":
        search_name = input("Enter name to search: ")
        found = False

        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(
                    f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}"
                )
                found = True

        if not found:
            print("No contact found")

    elif choice == "6":
        print(f"Total contacts: {len(contacts)}")

    elif choice == "7":
        print("Goodbye...")
        break

    else:
        print("Invalid input")
