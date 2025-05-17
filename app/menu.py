import flet as ft
from games.game import start_game

def create_menu(page: ft.Page):
    # Основное меню
    menu = ft.Column(
        [
            ft.Text(
                "Меню игры", 
                size=30, 
                weight=ft.FontWeight.BOLD, 
                color="yellow"
            ),
            ft.ElevatedButton(
                "Матемаика", 
                on_click=start_game, 
                style=ft.ButtonStyle(
                    color="black",  # Чёрный текст на кнопке
                    bgcolor="yellow",
                )
            ),
            ft.ElevatedButton(
                "Выход", 
                on_click=lambda e: page.window_close(),
                style=ft.ButtonStyle(
                    color="black",  # Чёрный текст на кнопке
                    bgcolor="yellow",
                )
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )
    return menu
