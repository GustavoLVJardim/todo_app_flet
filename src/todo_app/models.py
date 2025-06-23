import flet as ft

# estrutura de dados para representar uma tarefa
class Task():
    def __init__(self, title):
        self.title = title # texto descritivo da tarefa
        self.done = False # booleano (indica se foi concluída ou não)


    def to_dict(self):
        return {'title': self.title, 'done': self.done}