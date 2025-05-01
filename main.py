from task.task_manager import TaskManager

def main():
    manager = TaskManager()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Complete Task\n4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            manager.view_tasks()
        elif choice == "2":
            title = input("Task to add: ")
            due = input("Due date (optional): ")
            manager.add_task(title, due)
        elif choice == "3":
            manager.view_tasks()
            idx = int(input("Task to mark as complete: ")) - 1
            manager.complete_task(idx)
        elif choice == "4":
            break
        else:
            print("Option does not exist or is invalid!")

if __name__ == "__main__":
    main()
