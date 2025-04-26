# models.py

from utils import PATH, validate_and_parse_date as valid_date, save_data, generate_id

class TaskError(Exception):
    pass

class TitleError(TaskError):
    pass

class DateError(TaskError):
    pass

class Task:
    def __init__(self, title, description, due_date):
        if len(title) < 3 or len(title) > 30:
            raise TitleError("Title length must be greater than 3 and lower than 30 characters.")
        self._title = title
        
        if len(description) < 5 or len(description) > 50:
            raise TitleError("Description length must be greater than 5 and lower than 50 characters.")
        self._description = description
        
        validated_date = valid_date(due_date)
        if not validated_date:
            raise DateError("Invalid date format. Enter date format YYYY-MM-DD")
        self._due_date = validated_date
        
        self.id = generate_id(file_path=PATH)
        
        self.status = "Pending"
        
    def add_task(self, file_path=PATH):
        data = self.to_dict()
        save_data(data, file_path)
        return True
    
    def update_task(self):
        pass
    
    def delete_task(self):
        pass
    
    def view_tasks(self):
        pass
    
    def to_dict(self):
        data = {
            "id": self.id,
            "title": self._title,
            "description": self._description,
            "due_date": self._due_date.strftime("%Y-%m-%d") if self._due_date else None,
            "status": self.status
        }
        return data