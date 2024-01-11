# Importing the TaskManager class from the task_manager module
from task_manager import TaskManager

# Main part of the program
def main():
    # Creating an instance of the TaskManager class
    task_manager = TaskManager()

    # Menu loop for user interaction
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Completed")
        print("4. Remove Completed Tasks")
        print("5. Exit")

        # User input for menu choice
        choice = input("Enter your choice (1-5): ")

        # Handling user choices
        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            task_manager.mark_completed(task_index)
        elif choice == "4":
            task_manager.remove_completed_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the program
if __name__ == "__main__":
    main()
