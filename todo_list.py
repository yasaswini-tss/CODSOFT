tasks = []

while True:

    print("\n" + "=" * 40)
    print("           TO-DO LIST")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")
            for i, item in enumerate(tasks, start=1):
                status = "✓" if item["completed"] else "✗"
                print(f"{i}. {item['task']} [{status}]")

    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"'{removed['task']}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            task_num = int(input("Enter task number to mark completed: "))

            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")