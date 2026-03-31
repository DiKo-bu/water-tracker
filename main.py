import flet as ft
import time

def main(page: ft.Page):
    # --- Настройки страницы (Цвета и Центрирование) ---
    page.title = "Water Balance PRO"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F0F4F8" # Светло-серый фон
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # --- Переменные данных ---
    current_water = 0
    goal_water = 2000 # Цель в мл
    last_add_amount = 0

    # --- Цветовая палитра ---
    primary_blue = "#2196F3" # Основной синий
    dark_blue = "#1976D2"    # Темно-синий для кнопок
    light_blue = "#BBDEFB"   # Светло-синий для фона прогресса
    white = "#FFFFFF"

    # --- ФУНКЦИИ (Логика) ---

    def update_ui():
        """Обновляет все элементы интерфейса"""
        # Расчет процентов
        percent = current_water / goal_water
        if percent > 1.0: percent = 1.0
        
        # Обновление текста статуса
        status_text.value = f"{current_water} мл"
        status_percent.value = f"({int(percent * 100)}%)"
        
        # Обновление прогресс-бара (с плавной анимацией)
        progress_bar.value = percent
        
        # Меняем иконку, если цель достигнута
        if current_water >= goal_water:
            main_icon.icon = ft.icons.GPP_GOOD_ROUNDED
            main_icon.color = "green"
            status_text.color = "green"
        else:
            main_icon.icon = ft.icons.WATER_DROP_ROUNDED
            main_icon.color = primary_blue
            status_text.color = ft.colors.BLACK

        page.update()

    def add_water(amount):
        """Добавляет воду и запускает анимацию"""
        nonlocal current_water, last_add_amount
        if current_water >= goal_water: return # Уткнулись в цель

        last_add_amount = amount
        current_water += amount
        
        # Плавное обновление
        update_ui()
        
        # Показываем уведомление (Snackbar)
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Добавлено {amount} мл! 🎉"),
            bgcolor=primary_blue,
            action="OK"
        )
        page.snack_bar.open = True
        page.update()

    # --- ЭЛЕМЕНТЫ ДИЗАЙНА (UI) ---

    # 1. Главная иконка (сверху)
    main_icon = ft.Icon(
        name=ft.icons.WATER_DROP_ROUNDED,
        color=primary_blue,
        size=80,
        animate_scale=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
    )

    # 2. Текст статуса (Крупный и жирный)
    status_text = ft.Text(
        value="0 мл",
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        animate_opacity=300
    )
    
    # 3. Текст процентов (Поменьше)
    status_percent = ft.Text(
        value="(0%)",
        size=20,
        color=ft.colors.GREY_700,
        italic=True
    )

    # 4. Красивый Прогресс-бар (в карточке)
    progress_bar = ft.ProgressBar(
        value=0.0,
        width=300,
        height=15,
        color=primary_blue,
        bgcolor=light_blue,
        border_radius=ft.border_radius.all(10),
        animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT)
    )
    
    # Карточка для прогресс-бара
    progress_card = ft.Container(
        content=ft.Column([
            ft.Text("Дневной баланс", size=16, weight="bold"),
            progress_bar,
            status_percent,
        ], horizontal_alignment="center"),
        bgcolor=white,
        padding=20,
        border_radius=20,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.with_opacity(0.1, ft.colors.BLACK),
            offset=ft.Offset(0, 5)
        )
    )

    # 5. Кнопки добавления (Material 3 style)
    
    def build_add_button(amount, icon_name):
        """Создает стилизованную кнопку добавления"""
        return ft.Container(
            content=ft.Column([
                ft.Icon(name=icon_name, color=dark_blue, size=30),
                ft.Text(f"+{amount} мл", size=14, color=ft.colors.BLACK, weight="bold"),
            ], horizontal_alignment="center"),
            width=100,
            height=90,
            bgcolor=white,
            border_radius=15,
            padding=10,
            ink=True, # Эффект нажатия
            on_click=lambda _: add_water(amount),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.colors.with_opacity(0.05, ft.colors.BLACK),
                offset=ft.Offset(0, 2)
            ),
            animate_scale=ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        )

    btn_small = build_add_button(250, ft.icons.LOCAL_DRINK_ROUNDED)  # Стакан
    btn_med = build_add_button(500, ft.icons.WATER_ROUNDED)       # Мал. бутылка
    btn_large = build_add_button(1000, ft.icons.BEVERAGE_BOX_ROUNDED) # Большая тара

    # --- КОМПОНОВКА (Layout) ---
    
    page.add(
        ft.Column(
            [
                main_icon,
                status_text,
                ft.Container(height=10), # Отступ
                progress_card,
                ft.Container(height=30), # Отступ
                ft.Text("Добавить воды:", size=18, color=ft.colors.GREY_800),
                ft.Row(
                    [btn_small, btn_med, btn_large],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                ft.Container(height=20),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

    # Инициализация первого запуска
    update_ui()

# Запуск приложения
if __name__ == "__main__":
    # Используем современный ft.run вместо устаревшего ft.app
    ft.run(main, view=ft.AppView.WEB_BROWSER, port=8550)