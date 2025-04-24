Task Management CLI Application
Project Overview
Create a command-line task management application that allows users to create, view, update, and delete tasks. Tasks will be stored in a JSON file.
Technical Requirements

Create a GitHub repository named "python-task-manager"
Implement the following features:

Add a new task with title, description, and due date
List all tasks with option to filter by status (completed/pending)
Mark tasks as completed
Delete tasks
Search for tasks by keyword


Use proper error handling
Implement OOP principles with at least one class
Use file I/O operations to persist tasks between runs
Implement basic input validation

Project Structure
python-task-manager/
├── task_manager.py (main module)
├── models.py (Task class definition)
├── utils.py (helper functions)
├── tasks.json (data storage)
├── README.md (project documentation)
Implementation Details

Define a Task class with appropriate attributes and methods
Use context managers for file operations
Implement exception handling for file I/O and user input
Use JSON for data serialization
Create a simple command-line interface with a menu

Bonus (Optional)

Add task priority levels
Implement due date reminders
Add sorting options (by date, priority)
Use generators for task iteration