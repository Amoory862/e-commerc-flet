import flet as ft
from typing import Optional
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes 

class CustomButtonStyle(ft.ButtonStyle):
    def __init__(
        self,
        foreground_color: Optional[str] = None,
        background_color: Optional[str] = None,
        elevation: Optional[float] = None,
        padding: Optional[ft.PaddingValue] = None,
        side: Optional[ft.BorderSide] = None,
        shape: Optional[ft.OutlinedBorder] = None,
        disabled_foreground_color: Optional[str] = None,
        disabled_background_color: Optional[str] = None,
        text_style: Optional[ft.TextStyle] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.elevation = elevation
        self.padding = padding
        self.side = side
        self.shape = shape
        self.disabled_foreground_color = disabled_foreground_color
        self.disabled_background_color = disabled_background_color
        self.text_style = text_style

    def apply_style(self, button: ft.ButtonStyle):
        if self.foreground_color is not None:
            button.color = self.foreground_color
        if self.background_color is not None:
            button.bgcolor = self.background_color
        if self.elevation is not None:
            button.elevation = self.elevation
        if self.padding is not None:
            button.padding = self.padding
        if self.side is not None:
            button.side = self.side
        if self.shape is not None:
            button.shape = self.shape
        if self.disabled_foreground_color is not None:
            # Placeholder logic for disabled foreground color
            button.disabled_foreground_color = self.disabled_foreground_color  # Custom logic
        if self.disabled_background_color is not None:
            # Placeholder logic for disabled background color
            button.disabled_background_color = self.disabled_background_color  # Custom logic
        if self.text_style is not None:
            # Placeholder logic for text style
            button.text_style = self.text_style  # Custom logic

class ElevatedButtonThemeCustom:
    @staticmethod
    def light_theme():
        return CustomButtonStyle(
            foreground_color=TColors.light,
            background_color=TColors.primary,
            elevation=0,
            padding=ft.padding.symmetric(vertical=TSizes.button_height),
            side=ft.BorderSide(color=TColors.primary, width=0.1),
            shape=ft.RoundedRectangleBorder(radius=TSizes.button_radius),
            disabled_foreground_color=TColors.darkGrey,
            disabled_background_color=TColors.buttonDisabled,
            text_style=ft.TextStyle(size=16, color=TColors.textWhite, weight="w600")
        )

    @staticmethod
    def dark_theme():
        return CustomButtonStyle(
            foreground_color=TColors.light,
            background_color=TColors.primary,
            elevation=0,
            padding=ft.padding.symmetric(vertical=TSizes.button_height),
            side=ft.BorderSide(color=TColors.primary, width=1),
            shape=ft.RoundedRectangleBorder(radius=TSizes.button_radius),
            disabled_foreground_color=TColors.darkGrey,
            disabled_background_color=TColors.darkerGrey,
            text_style=ft.TextStyle(size=16, color=TColors.textWhite, weight="w600")
        )
