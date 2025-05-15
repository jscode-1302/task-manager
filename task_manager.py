# main file to instantiate our classes and try them
from models import TaskManager, Task

# Example usage
manager = TaskManager()

manager.list_tasks() # raise error

manager.add_task("Buy groceries", "Milk, eggs, bread", priority=3)
manager.add_task("Finish project", "Complete Python exercise", priority=5)
manager.add_task("Create CLI program", "Practice Python concepts", priority=2)
manager.add_task("Rent a car for roadtrip", "Save $300 for security deposit", priority=1)
manager.add_task("Make dinner", "Make venezuelan arepas before 8:00 pm", priority=6) # raise error

manager.complete_task(1)
manager.complete_task(1) # raise error

manager.delete_task(3)

print("Displaying tasks")
manager.list_tasks()  # Shows all tasks sorted by priority

print("-" * 40)
print("Searching for tasks")
manager.search("python") 

print("-" * 40)
print("Is task overdue?")
task = Task("Try is_overdue method", "It must return a message depends on whether is overdue", priority=3)
task.is_overdue()

manager.save_to_file(r'./tasks.json')