import flet as ft
from typing import Optional
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes

class OutlinedButtonStyleCustom(ft.ButtonStyle):
    def __init__(
        self,
        foreground_color: Optional[str] = None,
        border_side: Optional[ft.BorderSide] = None,
        text_style: Optional[ft.TextStyle] = None,
        padding: Optional[ft.PaddingValue] = None,
        shape: Optional[ft.OutlinedBorder] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.foreground_color = foreground_color
        self.border_side = border_side
        self.text_style = text_style
        self.padding = padding
        self.shape = shape

    def apply_style(self, button: ft.ButtonStyle):
        if self.foreground_color is not None:
            button.color = self.foreground_color
        if self.border_side is not None:
            button.side = self.border_side
        if self.text_style is not None:
            button.text_style = self.text_style
        if self.padding is not None:
            button.padding = self.padding
        if self.shape is not None:
            button.shape = self.shape

class OutlinedButtonThemeCustom:
    @staticmethod
    def light_theme():
        return OutlinedButtonStyleCustom(
            foreground_color=TColors.dark,
            border_side=ft.BorderSide(color=TColors.borderPrimary, width=1),
            text_style=ft.TextStyle(
                size=16,
                color=TColors.black,
                weight="w600"
            ),
            padding=ft.padding.symmetric(vertical=TSizes.button_height, horizontal=20),
            shape=ft.RoundedRectangleBorder(radius=TSizes.button_radius)
        )

    @staticmethod
    def dark_theme():
        return OutlinedButtonStyleCustom(
            foreground_color=TColors.light,
            border_side=ft.BorderSide(color=TColors.borderPrimary, width=1),
            text_style=ft.TextStyle(
                size=16,
                color=TColors.textWhite,
                weight="w600"
            ),
            padding=ft.padding.symmetric(vertical=TSizes.button_height, horizontal=20),
            shape=ft.RoundedRectangleBorder(radius=TSizes.button_radius)
        )
