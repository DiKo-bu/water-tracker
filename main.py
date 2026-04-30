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
        url="https://ottawa-descending-doctors-away.trycloudflare.com",
        width=page.width,
        height=page.height - 120,  # 40 — отступ под статус-бар, подбери под себя
        expand=True,
    )

    # Добавляем напрямую в страницу, без посредников
    page.add(webview)
   # page.add(ft.SafeArea(webview, top=True))
    # Обязательный пинок для отрисовки
    page.update()

ft.app(target=main)
