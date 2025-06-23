
import json
from models import Task

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            file_content = json.load(file)
            
            global_tasks = []
            for item in file_content:
                task = Task(item['title'], item['done'])
                global_tasks.append(task)
            return global_tasks

    except FileNotFoundError:
        return []
        
def save_tasks(tasks):
   
    with open('tasks.json', 'w') as file:
        dict_list = []
        for task in tasks:
            dict_list.append(task.to_dict())
        json.dump(dict_list, file, indent=4)