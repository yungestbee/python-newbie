# Simple contact book app

contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice =  input(f"Choose an Option: ")
    if choice == "1":
       name = input("Enter contact name: ")
       phone = input("Enter phone number: ")
       contacts[name] = phone
       print(f"Contact '{name}' added!")

    elif choice == "2":
       if contacts:
           print("your contacts")
           for name, phone in contacts.items():
               print(f"{name}: {phone}")
       else:
           print("No contacts yet")

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(f"{search}: {contacts[search]}")
        else:
            print("contact not found")

    elif choice == "4":
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print(f"Contact {delete} removed")
        else:
            print("Contact not found")

    elif choice == "5":
        print("GoodBye!")
        break

else:
    print("invalid choice picked")