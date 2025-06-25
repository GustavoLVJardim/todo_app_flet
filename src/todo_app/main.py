import flet as ft

from routes import home

def main(page: ft.Page):
    
    page.title = "Todo App"
    page.window.height = 600
    page.window.width = 370

    def route_change_handler(e):
        page.views.clear()
        view = home(page.route)
        if view:
            page.views.append(view(page))
        page.update()


    page.on_route_change = route_change_handler
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
