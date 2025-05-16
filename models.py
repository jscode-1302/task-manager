# Task and TaskManager classes
from datetime import datetime, timedelta
import os
import json

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
    
    def __init__(self, title, description, priority, completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.completed = completed   
        
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
        if days.days > 7:
            return True
        
    def __str__(self):
        return f"Id: {self.id} - Title: {self.title} - Description: {self.description} - Created at: {self.created_at} - Status {self.completed} - Priority: {self.priority}"
    
    def __repr__(self):
        return f"Task(id='{self.id}', title='{self.title}', description='{self.description}', created_at:'{self.created_at}', completed='{self.completed}', priority='{self.priority}')"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.id_counter = 1
        
    def add_task(self, title, description, priority):
        try:
            new_task = Task(title, description, priority)
            new_task.id = self.id_counter
            self.tasks.append(new_task)
            self.id_counter += 1
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
            return tasks
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
            return sorted_results
        except Exception as e:
            print(f"Error: {e}")
            
    def to_dict(self):
        try:
            if not self.tasks:
                raise EmptyListError("There's no data to parse")
            tasks = []
            for task in self.tasks:
                tasks.append({
                    'id': task.id,
                    'title': task.title,
                    'description': task.description,
                    'created_at': datetime.strftime(task.created_at, "%m/%d/%y"),
                    'completed': task.completed,
                    'priority': task.priority
                })
            return tasks
        except Exception as e:
            print(f"Error: {e}")
            
    def save_to_file(self, file):
        try:
            tasks = self.to_dict()
            with open(file, 'w') as f:
                json.dump(tasks, f, indent=2)
            return True
        except Exception as e:
            print(f"Error: {e}")
                
        
        