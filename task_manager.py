# task_manager.py

from models import Task, TaskManager
    
def create_task(title, description, due_date):
    tm = TaskManager()
    tm.load_tasks()
    task = Task(title, description, due_date)
    tm.add_task(task)
    tm.save_tasks()
    print("Task created successfully!")
    return True

def display_tasks():
    tm = TaskManager()
    tm.load_tasks()
    tasks = tm.view_tasks()
    for task in tasks:
        print(f"\033[31mId:\033[0m {task.id} - \033[31mTitle:\033[0m {task._title} - \033[31mDescription:\033[0m {task._description} - \033[31mDue date:\033[0m {task._due_date} - \033[31mStatus:\033[0m {task.status}")

def id_found(id):
    tm = TaskManager()
    tm.load_tasks()
    tm.save_tasks()
    found = tm.find_id(id)  
    return found
   
def modify_task(id):
    tm = TaskManager()
    tm.load_tasks()
    temp_task = tm.find_task(id)
    print("Modify and press enter: ")
    updated_task = Task(
        input(f"Title [{temp_task._title}]: ") or temp_task._title,
        input(f"Description [{temp_task._description}]: ") or temp_task._description,
        input(f"Due date [{temp_task._due_date}]: ") or temp_task._due_date,
        input(f"Status [{temp_task.status}]: ") or temp_task.status
    )
    temp_task.id = id
    tm.update_task(id, updated_task)
    print(f"Task N. {id} modified successfully!")
    return True
    
    
def main():
    print("Menu:\n1. Create a task\n2. View tasks\n3. Update a task\n4. Delete a task\n5. Search for tasks\n6. Exit")
    while True:
        try:
            option = int(input("\nEnter an option: "))
            if option == 6:
                print("Goodbye!")
                break
            elif option == 1:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date (YYYY-MM-DD): ")
                create_task(title, description, due_date)
            elif option == 2:
                display_tasks()
            elif option == 3:
                id = int(input("Enter task id to update: "))
                if id_found(id):
                    modify_task(id)
        except ValueError:
            print("Enter only integer numbers (1 - 6)")
        
if __name__ == "__main__":
    main()