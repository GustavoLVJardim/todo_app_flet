import flet as ft


def view_history(page: ft.Page):
    return ft.View(
        "/history",

        controls=[
            ft.Text("History"),
            ft.ElevatedButton(text="Back", on_click=lambda _: page.go('/'))
        ]

    )