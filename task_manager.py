# task_manager.py

from models import Task, TaskManager
    
def create_task(title, description, due_date):
    try:
        tm = TaskManager()
        task = Task(title, description, due_date)
        tm.add_task(task)
        print("Task created successfully!")
        return True
    except Exception as e:
        print(f"An error has ocurred: {e}")

def display_tasks():
    try:
        tm = TaskManager()
        tasks = tm.view_tasks()
        for task in tasks:
            print(f"\033[31mId:\033[0m {task.id} - \033[31mTitle:\033[0m {task._title} - \033[31mDescription:\033[0m {task._description} - \033[31mDue date:\033[0m {task._due_date} - \033[31mStatus:\033[0m {task.status}")
    except Exception as e:
        print(f"An error has ocurred: {e}")
    
def filter_tasks(task_status):
    try:
        if task_status not in ["Pending", "Completed"]:
            print("Status must be 'Pending' or 'Completed'.")
            return []
        tm = TaskManager()
        tasks = tm.view_tasks()
        filtered_tasks = list(filter(lambda x: x.status == task_status, tasks))
        for task in filtered_tasks:
            print(f"\033[31mId:\033[0m {task.id} - \033[31mTitle:\033[0m {task._title} - \033[31mDescription:\033[0m {task._description} - \033[31mDue date:\033[0m {task._due_date} - \033[31mStatus:\033[0m {task.status}")
    except Exception as e:
        print(f"An error has ocurred: {e}")
    
def id_found(id):
    try:
        tm = TaskManager()
        found = tm.find_id(id)  
        return found
    except Exception as e:
        print(f"An error has ocurred: {e}")
   
def modify_task(id):
    try:
        tm = TaskManager()
        temp_task = tm.find_task(id)
        print("Modify and press enter: ")
        updated_task = Task(
            input(f"Title [{temp_task._title}]: ") or temp_task._title,
            input(f"Description [{temp_task._description}]: ") or temp_task._description,
            input(f"Due date [{temp_task._due_date}]: ") or temp_task._due_date,
            input(f"Status [{temp_task.status}]: ") or temp_task.status
        )
        tm.update_task(id, updated_task)
        print(f"Task N. {id} modified successfully!")
        return True
    except Exception as e:
        print(f"An error has ocurred: {e}")

def remove_task(id):
    try:
        tm = TaskManager()
        tm.delete_task(id)
        print("Task deleted successfully!")
        return True
    except Exception as e:
        print(f"An error has ocurred: {e}")

def search_tasks_by_keyword(word):
    try:
        tm = TaskManager()
        tasks = tm.view_tasks()
        found_tasks = [task for task in tasks if word in task._title.lower() or word in task._description.lower()]
        if not found_tasks:
            print(f"No tasks found by '{word}'")
        for task in found_tasks:
            print(f"\033[31mId:\033[0m {task.id} - \033[31mTitle:\033[0m {task._title} - \033[31mDescription:\033[0m {task._description} - \033[31mDue date:\033[0m {task._due_date} - \033[31mStatus:\033[0m {task.status}")
    except Exception as e:
        print(f"An error has ocurred: {e}")
    
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
                task_status = input("\nEnter status to filter tasks: ")
                filter_tasks(task_status)
            elif option == 3:
                id = int(input("Enter task id to update: "))
                if id_found(id):
                    modify_task(id)
                else:
                    print("Id not found.")
            elif option == 4:
                id = int(input("Enter task id to delete: "))
                if id_found(id):
                    remove_task(id)
                else:
                    print("Id not found.")
            elif option == 5:
                word = input("Enter keyword: ")
                search_tasks_by_keyword(word.lower().strip())
            else:
                print("Option must be between 1 - 6")
        except ValueError:
            print("Enter only integer numbers (1 - 6)")
        
if __name__ == "__main__":
    main()