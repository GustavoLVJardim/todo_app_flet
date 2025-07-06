from todo_app.models.models import Task

#from todo_app.controllers.storage import load_tasks, save_tasks
from todo_app.controllers.firebase_controller import get_firestore_db, get_all_tasks_from_firestore

# funções que controlam a lógica do app (manipulam a lista de tarefas)
global_tasks = []

# lista onde cada tarefa é armazenada

def refresh_tasks():
    global global_tasks
    firestore_data = get_all_tasks_from_firestore()
    print("firestore_data:", firestore_data)
    global_tasks.clear()

    for item in firestore_data:
        task = Task(item['title'], item['done'], item['id'])
        global_tasks.append(task)

"""
def get_all_tasks(list_from_firestore):
    global_tasks = []
    for item in list_from_firestore:
        task = Task(item['title'], item['done'])
        global_tasks.append(task)
    return global_tasks
"""


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
    # 1. Conectar ao Firestore
    db = get_firestore_db()
    # 2. Acessar o documento pelo ID
    doc_ref = db.collection("tasks").document(task_to_remove.id)
    # 3. Deletar o documento
    doc_ref.delete()
    refresh_tasks()

    
        
def toggle_task(task_to_toggle):
    db = get_firestore_db()
    doc_ref = db.collection("tasks").document(task_to_toggle.id)
    new_status = not task_to_toggle.done
    doc_ref.update({"done": new_status})
    task_to_toggle.done = new_status # atualiza localmente também
    refresh_tasks()



def get_filtered_tasks(task_status):
    if task_status == "done": # Se o filtro for "done", retorna apenas tarefas concluídas (task.done == True)
        return [task for task in global_tasks if task.done]
    
    if task_status == "pending": # Se for "pending", retorna as não concluídas (task.done == False)
        return [task for task in global_tasks if not task.done]
    
    return global_tasks # Caso o filtro seja outro (ou vazio), retorna todas as tarefas.


            
    