# models.py

from utils import PATH, validate_and_parse_date as valid_date, generate_id, load_data
import json

class TaskError(Exception):
    pass

class TitleError(TaskError):
    pass

class DescriptionError(TaskError):
    pass

class DateError(TaskError):
    pass

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.validate_title(title)
        self.validate_description(description)
        self.validate_due_date(due_date)
        data = load_data()
        self.id = generate_id(data)
        self.status = status
    
    def to_dict(self):
        data = {
            "id": self.id,
            "title": self._title,
            "description": self._description,
            "due_date": self._due_date.strftime("%Y-%m-%d") if self._due_date else None,
            "status": self.status
        }
        return data
    
    def validate_title(self, title):
        if len(title) < 3 or len(title) > 30:
            raise TitleError("Title length must be greater than 3 and lower than 30 characters.")
        self._title = title
    
    def validate_description(self, description):
        if len(description) < 5 or len(description) > 50:
            raise DescriptionError("Description length must be greater than 5 and lower than 50 characters.")
        self._description = description
    
    def validate_due_date(self, due_date):
        validated_date = valid_date(due_date)
        if not validated_date:
            raise DateError("Invalid date format. Enter date format YYYY-MM-DD")
        self._due_date = validated_date
        
    def update_status(self, new_status):
        if new_status not in ["Pending", "Completed"]:
            raise ValueError("Status must be 'Pending' or 'Completed'.")
        self.status = new_status

class TaskManager:
    def __init__(self):
        self.tasks = []
            
    def load_tasks(self):
        data = load_data()
        for task_data in data.get("tasks", []):
            task = Task(
                title = task_data["title"],
                description = task_data["description"],
                due_date = task_data["due_date"],
                status = task_data.get("status", "Pending")
            )
            task.id = task_data["id"] # mantenemos id original porque el constructor genera uno nuevo
            self.tasks.append(task)
            
    def save_tasks(self):
        data = {"tasks": [task.to_dict() for task in self.tasks]}
        with open(PATH, "w") as f:
            json.dump(data, f, indent=2)

    def add_task(self, task):
        self.tasks.append(task)
    
    def update_task(self, id, updated_task):
        if self.find_id(id):
            for index, task in enumerate(self.tasks):
                if id == task.id:
                    self.tasks[index] = updated_task
                    updated_task.id = id # mantenemos id original porque el constructor genera uno nuevo
                    self.save_tasks()
                    break
        else:
            raise ValueError("Task ID not found.")
    
    def delete_task(self, id):
        pass
    
    def find_task(self, id):
        if self.find_id(id):
            for index, task in enumerate(self.tasks):
                if id == task.id:
                    return self.tasks[index]
    
    def find_id(self, id):
        for task in self.tasks:
            if id == task.id:
                return True
        return False
    
    def view_tasks(self):
        return self.tasks