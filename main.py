import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.BLACK  # чтобы не было белых артефактов

    def on_resize(e):
        webview.width = page.width
        webview.height = page.height
        page.update()

    webview = fwv.WebView(
        url="https://ottawa-descending-doctors-away.trycloudflare.com",
        expand=True,  # растягиваем на весь доступный контейнер
    )

    page.on_resized = on_resize
    page.add(webview)
    page.update()

ft.app(target=main)
