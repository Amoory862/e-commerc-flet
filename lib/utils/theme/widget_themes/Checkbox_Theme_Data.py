import flet as ft
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes

class TCheckboxTheme:
    @staticmethod
    def light_theme():
        return ft.CheckboxTheme(
            shape=ft.RoundedRectangleBorder(
                radius=TSizes.xs  
            ),
            check_color=TColors.white,
            fill_color=TColors.primary,
            overlay_color=TColors.grey,  
            splash_radius=20,  
            border_side=ft.BorderSide(color=TColors._black, width=2),  
            visual_density=ft.ThemeVisualDensity.COMFORTABLE,  
           
        )

    @staticmethod
    def dark_theme():
        return ft.CheckboxTheme(
            shape=ft.RoundedRectangleBorder(
                radius=TSizes.xs  
            ),
            check_color=TColors.white,
            fill_color=TColors.primary,
            overlay_color=TColors.grey,  
            splash_radius=20,  
            border_side=ft.BorderSide(color=TColors.white, width=2),  
            visual_density=ft.ThemeVisualDensity.COMFORTABLE,  
           
        )
