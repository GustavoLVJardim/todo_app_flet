import flet as ft


def view_config(page: ft.Page):
    return ft.View(
        "/config",

        controls=[
            ft.Text("Config"),
            ft.ElevatedButton(text="Back", on_click=lambda _: page.go('/'))
        ]

    )