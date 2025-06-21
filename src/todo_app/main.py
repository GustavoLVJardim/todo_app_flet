import flet as ft
from views import PageTaskView
from routes import home

def main(page: ft.Page):
    
    page.title = "Todo App"
    page.window.height = 600
    page.window.width = 370


    page.on_route_change = lambda e: home(page)
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
