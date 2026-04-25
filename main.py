import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.padding = 0

    # Создаем WebView с подменой User-Agent
    # Эта строка заставит Google думать, что ты заходишь через реальный Chrome
    webview = fwv.WebView(
        url="https://www.yandex.kz",
        expand=True,
        user_agent="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
    )

    layout = ft.Column(
        controls=[
            webview
        ],
        expand=True
    )

    page.add(layout)

ft.app(target=main)
