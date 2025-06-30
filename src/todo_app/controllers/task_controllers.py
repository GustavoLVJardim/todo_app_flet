from todo_app.models.models import Task

from todo_app.controllers.storage import load_tasks, save_tasks
from todo_app.controllers.firebase_controller import get_firestore_db

# funções que controlam a lógica do app (manipulam a lista de tarefas)

# lista onde cada tarefa é armazenada



def get_all_tasks(list_from_firestore):
    global_tasks = []
    for item in list_from_firestore:
        task = Task(item['title'], item['done'])
        global_tasks.append(task)
    return global_tasks


def add_task(title):
    """
    função add_task(título):
    obter conexão com o banco
    criar novo documento vazio na coleção "tasks"
    gravar {"title": título, "done": False} nesse documento
    """
    db = get_firestore_db()
    doc_ref = db.collection("tasks").document()
    doc_ref.set({
    "title": title,
    "done": False
    })

    return doc_ref


def remove_task(task_to_remove):
    if len(global_tasks) <= 0:
        return
    global_tasks.remove(task_to_remove)
    save_tasks(global_tasks)


def toggle_task(task_to_toggle):
    if len(global_tasks) <= 0:
        return
    task_to_toggle.done = not task_to_toggle.done
    save_tasks(global_tasks)


def get_filtered_tasks(task_status):
    done_tasks = []
    pending_tasks = []
    if task_status == "done":
        for task in global_tasks:
            if task.done:
                done_tasks.append(task)
        return done_tasks
    
    if task_status == "pending":
        for task in global_tasks:
            if not task.done:
                pending_tasks.append(task)
        return pending_tasks
    
    return global_tasks

            
    