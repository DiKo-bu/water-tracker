import flet as ft
def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.Text("Трекер воды: Готов к работе!", size=30, weight="bold"))
    page.add(ft.Icon(ft.icons.WATER_DROP, color="blue", size=100))
ft.app(target=main)
