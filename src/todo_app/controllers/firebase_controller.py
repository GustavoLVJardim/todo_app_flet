import firebase_admin
from firebase_admin import credentials, firestore

# inialize conection with firebase
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("/Users/utilizador/Desktop/codigos_python/flet_tutorials/my-app/src/todo-app-flet-firebase-adminsdk-fbsvc-f848643e09.json")
        firebase_admin.initialize_app(cred)

#get references to firestore
def get_firestore_db():
    initialize_firebase()
    return firestore.client()

# to save task
def save_task_in_firestore(task):
    db = get_firestore_db()
    # Deixa o Firestore criar o ID automático
    doc_ref = db.collection('tasks').document()  
    doc_ref.set(task.to_dict())

def get_all_tasks_from_firestore():
    list_tasks = []
    db = get_firestore_db()
    doc_ref = db.collection('tasks').get()
    for doc in doc_ref:
        list_tasks.append(doc.to_dict())
    return list_tasks


