import flet as ft
from lib.utils.constants.colors import TColors

class BottomSheetThemeCustom:
    @staticmethod
    def light_theme(content: str) -> ft.BottomSheet:
        return ft.BottomSheet(
            content=ft.Text(
                value=content,  # Use the provided variable text
                color=TColors.black  # Light theme text color
            ),
            open=True,
            elevation=4,  # Example elevation
            bgcolor=TColors.white,  # Light theme background color
            dismissible=True,
            enable_drag=True,
            show_drag_handle=True,
            use_safe_area=True,
            is_scroll_controlled=True,
            maintain_bottom_view_insets_padding=True,
            
        )

    @staticmethod
    def dark_theme(content: str) -> ft.BottomSheet:
        return ft.BottomSheet(
            content=ft.Text(
                value=content,  # Use the provided variable text
                color=TColors.white  # Dark theme text color
            ),
            open=True,
            elevation=4,  # Example elevation
            bgcolor=TColors.black,  # Dark theme background color
            dismissible=True,
            enable_drag=True,
            show_drag_handle=True,
            use_safe_area=True,
            is_scroll_controlled=True,
            maintain_bottom_view_insets_padding=True,
            
        )