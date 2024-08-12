import flet as ft 
from .widget_themes.Text_Theme import TTextTheme
from .widget_themes.Elevated_Button_Theme_Data import ElevatedButtonThemeCustom
from .widget_themes.Checkbox_Theme_Data import TCheckboxTheme
from .widget_themes.Chip_Theme_Data import ChipThemeCustom
from .widget_themes.Bottom_Sheet_Theme_Data import BottomSheetThemeCustom
from .widget_themes.App_Bar_Theme import AppBarThemeCustom
from .widget_themes.Outlined_Button_Theme import OutlinedButtonThemeCustom
from .widget_themes.Text_Field_Theme import TTextFieldTheme
from ..constants.colors import TColors

class CustomTheme(ft.Theme):
    def __init__(
        self,
        elevated_button_theme,
        outlined_button_theme,
        text_field_theme,
        bottom_sheet_theme,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.elevated_button_theme = elevated_button_theme
        self.outlined_button_theme = outlined_button_theme
        self.text_field_theme = text_field_theme
        self.bottom_sheet_theme = bottom_sheet_theme
        
    def apply_style(self, button: ft.ButtonStyle):
        if self.elevated_button_theme is not None:
            button.elevated_button_theme = self.elevated_button_theme
        if self.outlined_button_theme is not None:
            button.outlined_button_theme = self.outlined_button_theme
        if self.text_field_theme is not None:
            button.text_field_theme = self.text_field_theme
        if self.bottom_sheet_theme is not None:
            button.bottom_sheet_theme = self.bottom_sheet_theme
            
class AppTheme:
    def __init__(self):
        self.light_theme = self._create_light_theme()
        self.dark_theme = self._create_dark_theme()

    def _create_light_theme(self) -> ft.Theme:
        """Create and return the light theme configuration."""
        return CustomTheme(
            use_material3=True,
            font_family='Poppins',
            primary_color=TColors.primary,
            text_theme=TTextTheme.light_text_theme(),
            checkbox_theme=TCheckboxTheme.light_theme(),
            chip_theme=ChipThemeCustom.light_theme(),
            bottom_sheet_theme=BottomSheetThemeCustom.light_theme(content=''),
            appbar_theme=AppBarThemeCustom.light_theme(),
            color_scheme_seed=TColors.primary,
            primary_swatch=TColors.primary,
            elevated_button_theme=ElevatedButtonThemeCustom.light_theme(),
            outlined_button_theme=OutlinedButtonThemeCustom.light_theme(),
            text_field_theme=TTextFieldTheme.light_theme()
        )

    def _create_dark_theme(self) -> ft.Theme:
        """Create and return the dark theme configuration."""
        return CustomTheme(
            use_material3=True,
            font_family='Poppins',
            primary_color=TColors.primary,
            text_theme=TTextTheme.dark_text_theme(),
            checkbox_theme=TCheckboxTheme.dark_theme(),
            chip_theme=ChipThemeCustom.dark_theme(),
            bottom_sheet_theme=BottomSheetThemeCustom.dark_theme(content=''),
            appbar_theme=AppBarThemeCustom.dark_theme(),
            color_scheme_seed=TColors.primary,
            primary_swatch=TColors.primary,
            elevated_button_theme=ElevatedButtonThemeCustom.dark_theme(),
            outlined_button_theme=OutlinedButtonThemeCustom.dark_theme(),
            text_field_theme=TTextFieldTheme.dark_theme()
            
        )
 