import flet as ft
from todo_app.controllers.task_controllers import global_tasks, add_task, remove_task, toggle_task, refresh_tasks
from todo_app.models.debouncer import Debouncer
"""
A View é responsável por tudo o que o usuário vê e interage:
campos de texto, botões, listas, checkboxes etc.
Ela não processa regras de negócio — isso fica com o controller.
Ela apenas exibe os dados e dispara eventos que serão tratados
por outras camadas.
"""


# função que representa a tela principal
def PageTaskView(page: ft.Page):

    debouncer = Debouncer()

    def view_add_task(e):
       typed_text = input_user.controls[0].value
       if typed_text == '':
           return
       add_task(typed_text)
       input_user.controls[0].value = ''

       refresh_tasks()
       render_tasks()
       page.update()

    def view_remove_task(input_task):
        def remove_event(e):
            remove_task(input_task)

            refresh_tasks()
            render_tasks()
            page.update()
        return remove_event

    def view_toggle_task(input_task):

        def toggle_event(e):
            toggle_task(input_task)

            refresh_tasks()
            render_tasks()
            page.update()
        return toggle_event


    title = ft.Text("ToBuy App", size=30, weight='bold', color=ft.Colors.BLUE, text_align=ft.TextAlign.CENTER)

        
    input_user = ft.Row(
        controls=[
        ft.TextField(label="item"),
        ft.IconButton(icon=ft.Icons.ADD, on_click=view_add_task)
        ]
        
    )

    route_buttons = ft.Row(
        controls=[
        ft.IconButton(icon=ft.Icons.HISTORY, on_click=lambda _: page.go("/history?filter=done")),
        ft.IconButton(icon=ft.Icons.SETTINGS, on_click=lambda _: page.go('/config'))
        ]
        
    )
    
    
    
# When the user input will be show
    column = ft.Column()

# internal view's functions
    def render_tasks():
        column.controls.clear()
        

        for task in global_tasks:
            check_box = ft.Checkbox(label=task.title, value=task.done, on_change=lambda e, t=task: debouncer.debounce(toggle_task, t))
            delete_btn = ft.IconButton(icon=ft.Icons.DELETE, on_click=view_remove_task(task))
            row = ft.Row(controls=[check_box, delete_btn])
            column.controls.append(row)

    
    refresh_tasks()
    print("global_tasks after refresh:", global_tasks)
    render_tasks()

    return ft.View(
        "/",
        controls=[title, route_buttons, input_user, column],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
              