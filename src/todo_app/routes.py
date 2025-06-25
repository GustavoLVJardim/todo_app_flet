import flet as ft
from views import PageTaskView
from views_history import view_history
from views_config import view_config

def home(route):
    if route == "/":
        return PageTaskView

    elif route == "/history":
        return view_history

    elif route == "/config":
        return view_config
