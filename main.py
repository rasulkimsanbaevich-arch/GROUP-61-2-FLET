import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title="flet project"
    page.theme_mode = ft.ThemeMode.LIGHT  
    text = ft.Text(value="Hello world!")

    greeting_history = []
    history_text = ft.Text("История приветствий:")


    # functions
    def name_update(_):
        date =datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
        name = text_field.value
        if name:
            text_field.value = None
            text.color = None
            text.value = f'{date} - Hello, {name.title()}!'

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = "История приветствий: \n" + ", \n" .join(greeting_history)
        else:
            text.value = "Enter name!"
            text.color = ft.Colors.RED    

    def change_page(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

    def clear_button(e):
        print(greeting_history)
        greeting_history.clear()
        print(greeting_history)
        history_text.value = "История приветствий: "

    def sorte(_):
        greeting_history.sort()
        history_text.value = "История приветствий: \n" + ", \n" .join(greeting_history)
    def delete_f(_):
        if greeting_history:
            del greeting_history[-1:]
            print(greeting_history)
            history_text.value = "История приветствий: \n" + ", \n" .join(greeting_history)
        else: 
            history_text.value = "История пуста"    

    # buttons   
    elevated_button = ft.ElevatedButton("SEND", on_click=name_update)
    text_field = ft.TextField(label="Please enter name", expand=True)
    icon_button = ft.IconButton(icon=ft.Icons.FLARE_SHARP, on_click=change_page)
    clear_buttonn = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_button)
    sort = ft.IconButton(icon=ft.Icons.SORT, on_click=sorte) 
    delete_last = ft.ElevatedButton("del last", on_click=delete_f)


    my_object = ft.Row([text_field, elevated_button, icon_button, clear_buttonn, delete_last])
    


    page.add(text, my_object, sort, history_text)
ft.app(target=main)    