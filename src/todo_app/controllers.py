from models import Task

global_tasks = []

def add_task(title):
    task = Task(title)
    global_tasks.append(task)

def remove_task(task_to_remove):
    if len(global_tasks) <= 0:
        return
    global_tasks.remove(task_to_remove)

def toggle_task(task_to_toggle):
    if len(global_tasks) <= 0:
        return
    task_to_toggle.done = not task_to_toggle.done
