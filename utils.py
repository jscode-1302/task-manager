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

def read_file(file_path):
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

def load_data(file_path):
    data = read_file(file_path)
    if data: return data
        
def save_data(data, file_path):    
    existing_tasks = read_file(file_path)    
    
    # actualizamos con la info actual
    existing_tasks["tasks"].append(data)
    
    # escribimos de vuelta el archivo
    with open(file_path, "w") as f:
        json.dump(existing_tasks, f, indent=2)
        
def generate_id(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            return 1
 
    ids = [task.get("id", 1) for task in data["tasks"]]
    if len(ids) == 0:
        return 1
    else:
        return max(ids) + 1
    