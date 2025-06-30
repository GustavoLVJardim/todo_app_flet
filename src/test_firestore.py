from todo_app.models import Task
from todo_app.controllers.firebase_controller import save_task_to_firestore

# Criar uma tarefa de teste
task = Task(title="Teste Firebase", done=False)

# Salvar no Firestore
save_task_to_firestore(task)

print("Tarefa salva com sucesso!")
