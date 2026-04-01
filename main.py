import flet as ft

def main(page: ft.Page):
    # Добавляем текстовое поле
    page.add(ft.TextField(label="Введите текст"))

    # Добавляем кнопку
    page.add(ft.ElevatedButton(text="Кликнуть", on_click=lambda _: page.add(ft.Text("Вы нажали кнопку!"))))

if __name__ == "__main__":
    ft.app(target=main)
