import flet as ft
from datetime import datetime
from typing import List, Type, Optional, Any

class THelperFunctions:
    @staticmethod
    def get_color(value: str) -> Optional[str]:
        """Return color based on the given value."""
        color_map = {
            'Green': 'green',
            'Red': 'red',
            'Blue': 'blue',
            'Pink': 'pink',
            'Grey': 'grey',
            'Purple': 'purple',
            'Black': 'black',
            'White': 'white',
            'Yellow': 'yellow',
            'Orange': 'orange',
            'Brown': 'brown',
            'Teal': 'teal',
            'Indigo': 'indigo'
        }
        return color_map.get(value, None)

    @staticmethod
    def show_snackbar(page: ft.Page, message: str):
        """Display a snackbar with the given message."""
        page.add(ft.SnackBar(content=ft.Text(message)))

    @staticmethod
    def show_alert(page: ft.Page, title: str, message: str):
        """Display an alert dialog with the given title and message."""
        page.add(ft.AlertDialog(
            title=ft.Text(title),
            content=ft.Text(message),
            actions=[
                ft.TextButton(
                    text='OK',
                    on_click=lambda _: page.pop()
                )
            ]
        ))

    @staticmethod
    def navigate_to_screen(page: ft.Page, screen: ft.UserControl):
        """Navigate to the given screen."""
        page.go(screen)

    @staticmethod
    def truncate_text(text: str, max_length: int) -> str:
        """Truncate text to a specified length with ellipsis."""
        return text if len(text) <= max_length else f'{text[:max_length]}...'

    @staticmethod
    def is_dark_mode(theme: ft.Theme) -> bool:
        """Check if the current theme is dark mode."""
        return theme.mode == ft.ThemeMode.DARK

    @staticmethod
    def screen_size(page: ft.Page) -> tuple:
        """Return the screen size as a tuple (width, height)."""
        return page.window.width, page.window.height

    @staticmethod
    def screen_height(page: ft.Page) -> float:
        """Return the screen height."""
        return page.window.height

    @staticmethod
    def screen_width(page: ft.Page) -> float:
        """Return the screen width."""
        return page.window.width

    @staticmethod
    def get_formatted_date(date: datetime, format: str = 'dd MMM yyyy') -> str:
        """Return the date formatted as per the given format."""
        return date.strftime(format)

    @staticmethod
    def remove_duplicates(lst: List[Any]) -> List[Any]:
        """Remove duplicates from a list."""
        return list(set(lst))

    @staticmethod
    def wrap_widgets(widgets: List[ft.Control], row_size: int) -> List[ft.Row]:
        """Wrap a list of widgets into rows of specified size."""
        wrapped_list = []
        for i in range(0, len(widgets), row_size):
            row_children = widgets[i:i + row_size]
            wrapped_list.append(ft.Row(controls=row_children))
        return wrapped_list
