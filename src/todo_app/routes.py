import flet as ft
from todo_app.views.views import PageTaskView
from todo_app.views.views_history import view_history
from todo_app.views.views_config import view_config

def home(route, page):
    if route.startswith("/history"):
        return view_history(page)

    elif route.startswith("/config"):
        return view_config(page)

    elif route.startswith("/"):
        return PageTaskView(page)
