# Importing necessary modules for text coloring
from colorama import Fore, Style

# TaskManager class to manage tasks
class TaskManager:
    def __init__(self):
        # Lists to store active and completed tasks
        self.tasks = []
        self.completed_tasks = []

    # Method to add a new task
    def add_task(self, task):
        self.tasks.append(task)

    # Method to display active and completed tasks with text coloring
    def view_tasks(self):
        print("\nActive Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{Fore.RED}{index}. {task}{Style.RESET_ALL}")  # Red color for non-completed tasks

        print("\nCompleted Tasks:")
        for index, task in enumerate(self.completed_tasks, start=1):
            print(f"{Fore.GREEN}{index}. {task}{Style.RESET_ALL}")  # Green color for completed tasks

    # Method to mark a task as completed and move it to the completed_tasks list
    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            self.completed_tasks.append(completed_task)
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    # Method to remove all completed tasks
    def remove_completed_tasks(self):
        self.completed_tasks = []
        print("All completed tasks removed.")
