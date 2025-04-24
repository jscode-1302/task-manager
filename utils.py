# utils.py

from datetime import datetime
import json
import os

PATH = r'C:\Users\guapi\python-task-manager\tasks.json'

def validate_and_parse_date(date_string):
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        return date_object
    except ValueError:
        print("Invalid date format. Must be YYYY-MM-DD")
        return None
    
def save_data(data, file_path):
    existing_tasks = {}
        
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                try:
                    existing_tasks = json.load(f)
                except json.JSONDecodeError:
                    # File exists but isn't valid JSON - we'll use empty dict
                    pass
        except:
            # Handle any file reading errors - we'll use empty dict
            pass
    
    # Update with current game history
    existing_tasks.update(data)
    
    # Write back to file
    with open(file_path, "w") as f:
        json.dump(existing_tasks, f, indent=2)