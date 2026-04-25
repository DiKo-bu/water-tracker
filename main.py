import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    # Убираем все отступы, чтобы браузер был на весь экран
    page.padding = 0
    page.spacing = 0
    
    # Прямое создание компонента
    # Если на Яндексе будет белый экран — значит библиотека не хавает этот UA
    # Но этот вариант — самый стандартный для мобильного Chrome
    webview = fwv.WebView(
        url="https://www.yandex.kz",
        expand=True,
        user_agent="Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
    )

    # Добавляем напрямую в страницу, без посредников
    page.add(webview)
    
    # Обязательный пинок для отрисовки
    page.update()

ft.app(target=main)
