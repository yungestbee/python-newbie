# Simple Notes App

def add_note():
    note = open("NewText.txt", "a")
    note.write(input("Enter you notes here: "))
    print("Note added")

def view_notes():
    note = open("NewText.txt", "r")
    print(note.read())

def clear_notes():
    note = open("NewText.txt", "w")
    note.write(" ")

while True:
    print("\n1. Add Note\n2. View Notes\n3. Clear Notes\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        clear_notes()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please select a valid option.")
