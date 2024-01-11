# Task Manager - Python

A basic Python project for managing tasks through a command-line interface. The project includes a `TaskManager` class with functionalities such as adding tasks, viewing tasks, marking tasks as completed, and removing completed tasks.

## Features:

- **Add Task:** Enter a new task to be managed.
- **View Tasks:** Display a list of both active and completed tasks with color-coded formatting.
- **Mark as Completed:** Mark a task as completed and move it to the completed tasks list.
- **Remove Completed Tasks:** Clear all completed tasks from the list.
  
## Object-Oriented Programming (OOP) Principles:

- **Encapsulation:**
  - **Usage:** The `TaskManager` class encapsulates the data and methods related to task management within a single class, providing a clear and modular structure.

- **Abstraction:**
  - **Usage:** The methods of the `TaskManager` class abstract the underlying details of task management, allowing users (in this case, the main program) to interact with the class without needing to know the internal implementation.

## Problem-Solving Approach:

- **User-Centric Design:**
  - **Approach:** The design of the `TaskManager` class and the main program (`main.py`) prioritizes user interaction. The menu-driven interface and clear instructions make it easy for users to add, view, and manage tasks without unnecessary complexity.

- **Error Handling:**
  - **Approach:** The code includes error handling for invalid user inputs, such as checking if the task index is within a valid range. This helps prevent unexpected issues and provides feedback to users when an error occurs.

- **Readability and Maintainability:**
  - **Approach:** The code is structured with clear and descriptive method names, comments, and a modular design. This approach enhances readability and makes the code more maintainable, allowing for future modifications or additions.

- **Version Control (Git):**
  - **Approach:** The use of Git for version control reflects a proactive approach to managing code changes collaboratively. It allows for tracking project history, managing branches, and facilitating collaboration with others.
