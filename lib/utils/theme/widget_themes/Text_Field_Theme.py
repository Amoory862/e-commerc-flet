import flet as ft
from typing import Optional
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes


class TTextFieldTheme:
    @staticmethod
    def light_theme():
        return ft.TextField(
            label="Label Text",
            hint_text="Hint Text",
            prefix_icon=ft.Icon(name="icon_name", color=TColors.darkGrey),
            suffix_icon=ft.Icon(name="icon_name", color=TColors.darkGrey),
            border=ft.border_radius.all(2)
            ,
            focused_border_color=TColors.dark,
            label_style=ft.TextStyle(
                size=TSizes.font_size_md,
                color=TColors.black
            ),
            hint_style=ft.TextStyle(
                size=TSizes.font_size_sm,
                color=TColors.black
            ),
            error_text="Error message here",  # Add error message handling as needed
            content_padding=ft.padding.symmetric(vertical=TSizes.input_field_radius),
        )

    @staticmethod
    def dark_theme():
        return ft.TextField(
            label="",
            hint_text="Hint Text",
            prefix_icon=ft.Icon(name="icon_name", color=TColors.darkGrey),
            suffix_icon=ft.Icon(name="icon_name", color=TColors.darkGrey),
            border=ft.border_radius.all(2)
            ,
            label_style=ft.TextStyle(
                size=TSizes.font_size_md,
                color=TColors.white
            ),
            hint_style=ft.TextStyle(
                size=TSizes.font_size_sm,
                color=TColors.white
            ),
            error_text="Error message here",  # Add error message handling as needed
            content_padding=ft.padding.symmetric(vertical=TSizes.input_field_radius),
        )
