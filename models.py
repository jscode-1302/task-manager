# Task and TaskManager classes
from datetime import datetime

class TaskError(Exception):
    pass

class TaskAlreadyCompletedError(TaskError):
    pass

class EmptyListError(TaskError):
    pass

def validate_overdue(func):
    def wrapper(*args, **kwargs):
        overdue = func(*args)
        if overdue:
            print("Task is overdue. Please check it as soon as possible.")
            return overdue
        print("Task is up to date")
        return overdue
    return wrapper

class Task:
    id = 1
    
    def __init__(self, title, description, priority, created_at=datetime.now(), completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.created_at = created_at
        self.completed = completed
        self.id = Task.id
        
        Task.id += 1
        
    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, value):
        if value not in range(1, 6):
            raise ValueError("Priority must be between 1 - 5.")
        self._priority = value
    
    @validate_overdue 
    def is_overdue(self):
        days = datetime.now() - self.created_at
        if days > 7:
            return True
        
    def __str__(self):
        return f"Id: {self.id} - Title: {self.title} - Description: {self.description} - Created at: {self.created_at} - Status {self.completed} - Priority: {self.priority}"
    
    def __repr__(self):
        return f"Task(id='{self.id}', title='{self.title}', description='{self.description}', created_at:'{self.created_at}', completed='{self.completed}', priority='{self.priority}')"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, title, description, priority):
        try:
            new_task = Task(title, description, priority)
            self.tasks.append(new_task)
            return True
        except ValueError as e:
            print(f"Error: {e}")
            
    def delete_task(self, id):  
        for index, task in enumerate(self.tasks):
            if id == task.id:
                del self.tasks[index]
                return True
        return False
    
    def complete_task(self, id):
        for task in self.tasks:
            if id == task.id:
                try:
                    if not task.completed:
                        task.completed = True
                        return True
                    else:
                        raise TaskAlreadyCompletedError("Task is already completed")
                except Exception as e:
                    print(f"Error: {e}")
        return False
    
    def list_tasks(self):
        try:
            if not self.tasks:
                raise EmptyListError("No tasks to display")
            tasks = sorted(self.tasks, key= lambda x: x.priority)
            for task in tasks:
                print(f"Id: {task.id} - Title: {task.title} - Description: {task.description} - Created at: {task.created_at} - Status {task.completed} - Priority: {task.priority}")
        except Exception as e:
            print(f"Error: {e}")
            
    def search(self, word):
        try:
            if not self.tasks:
                raise EmptyListError("No tasks to display")
            results = list(task for task in self.tasks if word.lower() in task.title.lower() or word.lower() in task.description.lower())
            if not results:
                return []
            sorted_results = sorted(results, key= lambda x: x.priority)
            for task in sorted_results:
                print(f"Id: {task.id} - Title: {task.title} - Description: {task.description} - Created at: {task.created_at} - Status {task.completed} - Priority: {task.priority}")
        except Exception as e:
            print(f"Error: {e}")