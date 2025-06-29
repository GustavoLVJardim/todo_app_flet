from todo_app.models.models import Task

from todo_app.controllers.storage import load_tasks, save_tasks



# funções que controlam a lógica do app (manipulam a lista de tarefas)

# lista onde cada tarefa é armazenada
global_tasks = load_tasks()

# Cria uma nova instância de Task
# Adiciona à lista global_tasks
def add_task(title):
    task = Task(title)
    global_tasks.append(task)
    save_tasks(global_tasks)

# Remove uma tarefa da lista com base no índice
# Só remove se o índice for válido
def remove_task(task_to_remove):
    if len(global_tasks) <= 0:
        return
    global_tasks.remove(task_to_remove)
    save_tasks(global_tasks)

# Altera o status done da tarefa no índice especificado
# De False para True e vice-versa
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

            
    