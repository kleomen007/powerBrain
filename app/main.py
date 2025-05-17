import flet as ft
from menu import create_menu

def main(page: ft.Page):
    # Настройка страницы
    page.title = "Игра: Верно или неверно"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "darkblue"  # Тёмно-синий фон

    # Отображаем менюs
    menu = create_menu(page)
    page.add(menu)

ft.app(target=main)

'''     
# Чтение вопросов из файлов с учетом пути
def read_questions(folder1, folder2, filename):
    file_path = os.path.join(folder1, folder2, filename)  # Путь к файлу
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {filename} не найден!")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

correct_answers = read_questions("games", "math", "yes_math_58.txt")
        incorrect_answers = read_questions("games", "math", "no_math_58.txt")
'''