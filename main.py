import flet as ft
import flet_webview as fwv

def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0

    webview = fwv.WebView(
        url="https://your-url.trycloudflare.com",
        expand=True,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(height=40),  # отступ под статус-бар, подбери 30-50
                webview,
            ],
            spacing=0,
            expand=True,
        )
    )
    page.update()

ft.app(target=main)
