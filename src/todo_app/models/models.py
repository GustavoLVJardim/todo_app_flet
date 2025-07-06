import flet as ft

# estrutura de dados para representar uma tarefa
class Task():
    def __init__(self, title, done=False, id=None):
        self.title = title # texto descritivo da tarefa
        self.done = done # booleano (indica se foi concluída ou não)
        self.id = id


    def to_dict(self):
        return {'title': self.title, 'done': self.done}