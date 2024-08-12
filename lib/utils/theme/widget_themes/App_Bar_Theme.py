import flet as ft
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes

class AppBarThemeCustom:
    @staticmethod
    def light_theme():
        return ft.AppBarTheme(
            bgcolor=ft.colors.TRANSPARENT,  # Background color
            color=TColors.black,  # Foreground color (e.g., for icons and text)
            shadow_color=TColors.grey,  # Shadow color
            surface_tint_color=ft.colors.TRANSPARENT,  # Surface tint color
            elevation=0,  # Elevation
            title_text_style=ft.TextStyle(
                size=18.0,
                weight="w600",
                color=TColors.black
            ),
            center_title=False,
            scroll_elevation=0,
            toolbar_height=TSizes.app_bar_height,
        )
 
    @staticmethod
    def dark_theme():
        return ft.AppBarTheme(
            bgcolor=ft.colors.TRANSPARENT,  # Background color
            color=TColors.white,  # Foreground color (e.g., for icons and text)
            shadow_color=TColors.darkerGrey,  # Shadow color
            surface_tint_color=ft.colors.TRANSPARENT,  # Surface tint color
            elevation=0,  # Elevation
            title_text_style=ft.TextStyle(
                size=18.0,
                weight="w600",
                color=TColors.white
            ),
            center_title=False,
            scroll_elevation=0,
            toolbar_height=TSizes.app_bar_height,
        )
