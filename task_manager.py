# task_manager.py

from models import Task

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
                if len(due_date.split("-")) != 3:
                    print("Invalid format. Please use YYYY-MM-DD")
                try:
                    new_task = Task(title, description, due_date)
                    new_task.add_task()
                except Exception as e:
                    print(f"Error: {e}")
        except ValueError:
            print("Enter only integer numbers (1 - 6)")
        
        
if __name__ == "__main__":
    main()