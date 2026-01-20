from task_manager import Taskmanager
def main():
    manager = Taskmanager()
    while True:
        print("\n--- SMART TASK MANAGER ---")
        print("1. Add Task")
        print("2. view Tasks")
        print("3. Exit")

        choice = input("Choose option:")
        if choice == "1":
            title = input("Enter task title:")
            manager.add_task(title)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            print("Exiting...Bye!👋")
            break
        else:
            print("invalid choice❌,try again")
if __name__ == "__main__":
    main()