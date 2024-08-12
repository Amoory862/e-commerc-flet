import flet as ft
from lib.utils.constants.colors import TColors

class TTextTheme:
    @staticmethod
    def light_text_theme():
        return ft.TextTheme(
            headline_large=ft.TextStyle(size=32, weight="bold", color=TColors.dark),
            headline_medium=ft.TextStyle(size=24, weight="w600", color=TColors.dark),
            headline_small=ft.TextStyle(size=18, weight="w600", color=TColors.dark),

            title_large=ft.TextStyle(size=16, weight="w600", color=TColors.dark),
            title_medium=ft.TextStyle(size=16, weight="w500", color=TColors.dark),
            title_small=ft.TextStyle(size=16, weight="w400", color=TColors.dark),

            body_large=ft.TextStyle(size=14, weight="w500", color=TColors.dark),
            body_medium=ft.TextStyle(size=14, weight="normal", color=TColors.dark),
            body_small=ft.TextStyle(size=14, weight="w500", color="#80000000"),  # Using hex code with transparency

            label_large=ft.TextStyle(size=12, weight="normal", color=TColors.dark),
            label_medium=ft.TextStyle(size=12, weight="normal", color="#80000000")  # Using hex code with transparency
        )

    @staticmethod
    def dark_text_theme():
        return ft.TextTheme(
            headline_large=ft.TextStyle(size=32, weight="bold", color=TColors.light),
            headline_medium=ft.TextStyle(size=24, weight="w600", color=TColors.light),
            headline_small=ft.TextStyle(size=18, weight="w600", color=TColors.light),

            title_large=ft.TextStyle(size=16, weight="w600", color=TColors.light),
            title_medium=ft.TextStyle(size=16, weight="w500", color=TColors.light),
            title_small=ft.TextStyle(size=16, weight="w400", color=TColors.light),

            body_large=ft.TextStyle(size=14, weight="w500", color=TColors.light),
            body_medium=ft.TextStyle(size=14, weight="normal", color=TColors.light),
            body_small=ft.TextStyle(size=14, weight="w500", color="#80F6F6F6"),  # Using hex code with transparency

            label_large=ft.TextStyle(size=12, weight="normal", color=TColors.light),
            label_medium=ft.TextStyle(size=12, weight="normal", color="#80F6F6F6")  # Using hex code with transparency
        )
