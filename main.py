import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title="flet project"
    page.theme_mode = ft.ThemeMode.LIGHT

    
    
  
    text = ft.Text(value="Hello world!")


    # functions
    def name_update(_):
        date =datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
        name = text_field.value
        if name:
            text.color = None
            text.value = f'{date} - Hello, {name.title()}!'
        else:
            text.value = "Enter name!"
            text.color = ft.Colors.RED    

    def change_page(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

    # buttons
    elevated_button = ft.ElevatedButton("SEND", on_click=name_update)
    text_field = ft.TextField(label="Please enter name")
    icon_button = ft.IconButton(icon=ft.Icons.FLARE_SHARP, on_click=change_page)







    page.add(text, text_field, elevated_button, icon_button)
ft.app(target=main)    