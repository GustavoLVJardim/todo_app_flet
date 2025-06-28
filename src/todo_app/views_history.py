import flet as ft
from urllib.parse import urlparse, parse_qs
from controllers import *
from views import *


def view_history(page: ft.Page):

    def get_parameters():
        route = page.route
        parsed_url = urlparse(route)
        dict_url_parameter = parse_qs(parsed_url.query)
        
        if dict_url_parameter.get("filter"):
            filter = dict_url_parameter.get("filter")[0]
            return filter
        
        return None
        
    filter = get_parameters()
    print(f"filter: {filter}")
    filtered_tasks = get_filtered_tasks(filter)
    print(f"filtered_tasks: {filtered_tasks}")

    row_btn = ft.Row(
        controls=[
            ft.TextButton(text="All", on_click= lambda _: page.go('/history?filter=all')),
            ft.TextButton(text="Done", on_click= lambda _: page.go('/history?filter=done')),
            ft.TextButton(text="Pending", on_click= lambda _: page.go('/history?filter=pending'))
        ],
        alignment=ft.MainAxisAlignment.CENTER
        
        
        
    )


    column =ft.Column()

    for task in filtered_tasks:
        hist_tasks = ft.Checkbox(label=task.title)
        row = ft.Row(controls=[hist_tasks])
        column.controls.append(row)

    if len(filtered_tasks) == 0:
        column.controls.append(ft.Text("No tasks found"))


    
    view = ft.View(
        "/history",

        controls=[
            ft.Text("History"),
            ft.ElevatedButton(text="Back", on_click=lambda _: page.go('/')),
            row_btn,
            column
        ]

    )

    return view