import flet as ft
import random, time
import os

# Чтение вопросов из файлов с учетом пути
def read_questions(folder1, folder2, filename):
    file_path = os.path.join(folder1, folder2, filename)  # Путь к файлу
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {filename} не найден!")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

# Функция для запуска игры
def start_game(e):
    page = e.page
    page.clean()

    try:
        # Считываем верные и неверные ответы из файлов
        correct_answers = read_questions("games", "math", "yes_math_58.txt")
        incorrect_answers = read_questions("games", "math", "no_math_58.txt")
    except FileNotFoundError as ex:
        page.add(ft.Text(str(ex), size=24, color="red"))
        page.update()
        return

     # Переменные игры
    total_questions = 20
    correct_count = 0
    answered_questions = 0
    total_time = 20  # Время на игру (в секундах)
    start_time = time.time()  # Засекаем время начала игры

    # Функция для проверки времени
    def check_time():
        elapsed_time = time.time() - start_time
        if elapsed_time >= total_time:
            return True  # Время истекло
        return False

    # Выбор случайного вопроса
    def get_next_question():
        nonlocal answered_questions
        nonlocal correct_count

        # Проверяем время
        if check_time():
            # Время истекло, выводим результат
            page.clean()
            page.add(ft.Text(f"Время вышло! Правильных ответов: {correct_count} из {total_questions}", size=24, color="red"))
            page.add(ft.Row(
                [
                    ft.ElevatedButton("Играть снова", on_click=start_game, style=ft.ButtonStyle(color="black", bgcolor="yellow")),
                    ft.ElevatedButton("В меню", on_click=lambda e: return_to_menu(page), style=ft.ButtonStyle(color="black", bgcolor="yellow"))
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ))
            page.update()
            return

        if answered_questions >= total_questions:
            # Игра закончена, выводим результат
            page.clean()
            page.add(ft.Text(f"Игра завершена! Правильных ответов: {correct_count} из {total_questions}", size=24, color="yellow"))
            page.add(ft.Row(
                [
                    ft.ElevatedButton("Играть снова", on_click=start_game, style=ft.ButtonStyle(color="black", bgcolor="yellow")),
                    ft.ElevatedButton("В меню", on_click=lambda e: return_to_menu(page), style=ft.ButtonStyle(color="black", bgcolor="yellow"))
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ))
            page.update()
            return

        # Считываем вопросы и выбираем случайный
        question = random.choice(correct_answers + incorrect_answers)

        # Показываем номер текущего вопроса
        page.add(ft.Text(f"Вопрос {answered_questions + 1} из {total_questions}", size=18, color="yellow"))
        page.add(ft.Text(f"Оставшееся время: {total_time - int(time.time() - start_time)} сек", size=18, color="yellow"))
        page.add(ft.Text(question, size=24, color="yellow"))

        # Функция для проверки правильности ответа
        def check_answer(is_correct: bool):
            nonlocal correct_count
            nonlocal answered_questions

            if (question in correct_answers and is_correct) or (question in incorrect_answers and not is_correct):
                correct_count += 1

            answered_questions += 1
            page.clean()
            get_next_question()  # Переход к следующему вопросу

        # Кнопки для выбора ответа
        page.add(ft.Row(
            [
                ft.IconButton(ft.icons.CHECK, icon_size=40, on_click=lambda e: check_answer(True), style=ft.ButtonStyle(bgcolor="green")),
                ft.IconButton(ft.icons.CANCEL, icon_size=40, on_click=lambda e: check_answer(False), style=ft.ButtonStyle(bgcolor="red"))
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ))

        page.update()

    get_next_question()

# Функция возврата в меню
def return_to_menu(page):
    from menu import create_menu
    page.clean()
    menu = create_menu(page)
    page.add(menu)
    page.update()