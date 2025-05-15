import os
import json

def get_id(file):
    if not os.path.exists(file):
        raise FileNotFoundError("File not found")
    
    if os.stat(file).st_size == 0:
        return 1
    
    with open(file, 'r') as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            return 1
        if not isinstance(tasks, list) or not tasks:
            return 1

        ids = [task.get('id', 0) for task in tasks if isinstance(task, dict)]
        return max(ids, default=0) + 1