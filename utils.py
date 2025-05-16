import os
import json

def get_id(file):
    if not os.path.exists(file):
        return 1
    try:
        with open(file, 'r') as f:
            tasks = json.load(f)   
        ids = [task.get('id', 1) for task in tasks if isinstance(task, dict)]
        return max(ids, default=1) + 1

    except json.JSONDecodeError as e:
        return 1