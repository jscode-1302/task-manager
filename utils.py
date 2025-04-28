# utils.py

from datetime import datetime, date
import json
import os

PATH = r'C:\Users\guapi\python-task-manager\tasks.json'
    
def validate_and_parse_date(date_string):
    if isinstance(date_string, (date, datetime)):
        return date_string
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        return date_object
    except ValueError:
        print("Invalid date format. Must be YYYY-MM-DD")
        return None

def read_file(file_path=PATH):
    existing_data = {"tasks": []}
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    # archivo existe pero no es un JSON valido - usamos el diccionario vacio
                    return existing_data
        except:
            # manejamos cualquier otro error de lectura - usamos un diccionario vacio
            return existing_data

def load_data(file_path=PATH):
    data = read_file(file_path)
    if data: return data
        
def generate_id(data):
    ids = [task.get("id", 1) for task in data.get("tasks", [])]
    if not ids:
        return 1
    else:
        return max(ids) + 1

    