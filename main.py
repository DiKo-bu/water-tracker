import flet
from flet import Page, Column, TextField, Text, SafeArea, MainAxisAlignment, CrossAxisAlignment, Container, padding, Colors

def main(page: Page):
    page.title = "Dynamic Text Example"
    page.padding = padding.all(20)          # единые отступы со всех сторон
    page.horizontal_alignment = "center"    # центрирование по горизонтали
    page.scroll = "adaptive"                # позволит скроллить, если клавиатура поднимет контент

    # Поле ввода — адаптивное, без жёсткой ширины
    input_field = TextField(
        label="Введите текст",
        hint_text="Начните печатать...",
        text_size=18,
        border_radius=15,
        bgcolor=Colors.WHITE,
        filled=True,                        # заливка фона
        content_padding=padding.symmetric(horizontal=16, vertical=12),  # внутренние отступы
    )

    text_label = Text(
        "",
        size=22,
        weight="bold",
        color=Colors.BLUE_800,
        text_align="center",                # центрирование текста
    )

    def update_text(e):
        text_label.value = input_field.value if input_field.value else " "  # чтобы не схлопывался
        page.update()

    input_field.on_change = update_text

    # Основной контент с вертикальным центрированием, но с отступом сверху
    column = Column(
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
