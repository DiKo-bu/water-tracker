import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    # Убираем лишние отступы по краям экрана
    page.padding = 0

    # Создаем встроенный браузер
    webview = fwv.WebView(
        url="https://google.com",
        expand=True
    )

    # Главный контейнер с идеальными отступами для controls
    layout = ft.Column(
        controls=[
            webview
        ],
        expand=True
    )

    # Добавляем контейнер на страницу
    page.add(layout)

ft.app(target=main)
