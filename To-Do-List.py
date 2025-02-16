# Simple To-Do List Manager
tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        if tasks:
            for i in range(len(tasks)):
                print(tasks[i])
        else:
            print("No tasks yet!")

    elif choice == "3":
        task_number = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed = tasks.pop(task_number)
            print(f"Task '{removed}' removed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please choose a valid option.")
