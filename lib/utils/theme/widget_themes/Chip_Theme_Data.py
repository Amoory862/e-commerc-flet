import flet as ft
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes

class ChipThemeCustom:
    
    @staticmethod
    def light_theme():
        return ft.ChipTheme(
            disabled_color=TColors.grey,  # Adjust opacity
            label_text_style=ft.TextStyle(
                color=TColors.black
            ),
            selected_color=TColors.primary,
            padding=ft.padding.symmetric(vertical=12, horizontal=12),  # Adjust padding
            checkmark_color=TColors.white
        )

    @staticmethod
    def dark_theme():
        return ft.ChipTheme(
            disabled_color=TColors.darkerGrey,
            label_text_style=ft.TextStyle(
                color=TColors.white
            ),
            selected_color=TColors.primary,
            padding=ft.padding.symmetric(vertical=12, horizontal=12),  # Adjust padding
            checkmark_color=TColors.white
        )
