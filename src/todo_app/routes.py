import flet as ft
from views import PageTaskView

def home(page: ft.Page):
    if page.route == "/":
        page.views.clear()
        page.views.append(PageTaskView(page))
        page.update()
