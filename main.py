import flet as ft
import flet_webview as fwv


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0

    def on_navigation(e):
        e.prevent_default = False
        page.update()

    webview = fwv.WebView(
        url="https://donald-open-bookmark-roulette.trycloudflare.com",
        expand=True,
        javascript_enabled=True,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(height=40),
                webview,
            ],
            spacing=0,
            expand=True,
        )
    )
    page.update()


ft.app(target=main)
