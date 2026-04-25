import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.title = "Приложение со встроенным браузером"
    
    # Создаем компонент WebView
    # Параметр expand=True заставляет его растянуться на весь экран
    webview = fwv.WebView(
        url="https://flet.dev",
        expand=True,
        on_page_started=lambda _: print("Началась загрузка страницы..."),
        on_page_ended=lambda _: print("Страница полностью загружена!")
    )
    
    # Добавляем его на страницу как обычный элемент
    page.add(webview)

ft.app(target=main)
        controls=[
            Container(height=20),            # отступ сверху
            input_field,
            Container(height=30),            # воздух между полем и текстом
            text_label,
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=0,                          # используем Container для точного контроля
        expand=True,                        # растягивает колонку по высоте
    )

    # SafeArea гарантирует, что ничто не залезет под вырез экрана или системные панели
    content = SafeArea(
        column,
        expand=True,
    )

    page.add(content)

flet.app(target=main)
