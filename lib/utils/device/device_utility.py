import flet as ft
import platform
import socket
import webbrowser
import asyncio

class TDeviceUtils:
    @staticmethod
    def hide_keyboard(page):
        # Flet automatically manages the keyboard, no direct equivalent.
        page.update()

    @staticmethod
    def set_status_bar_color(color):
        # No direct method to change status bar color in Flet.
        pass

    @staticmethod
    def is_landscape_orientation(page):
        return page.window_width > page.window_height

    @staticmethod
    def is_portrait_orientation(page):
        return page.window_height > page.window_width

    @staticmethod
    def set_full_screen(enable, page):
        # Not directly supported by Flet, might use browser options for web.
        pass

    @staticmethod
    def get_screen_height(page):
        return page.window_height

    @staticmethod
    def get_screen_width(page):
        return page.window_width

    @staticmethod
    def get_pixel_ratio(page):
        # Scale factor is used instead of pixel ratio in Flet.
        return page.scale_factor

    @staticmethod
    def get_status_bar_height():
        # No direct equivalent in Flet.
        return 0

    @staticmethod
    def get_bottom_navigation_bar_height():
        return 56  # Standard height in most UIs

    @staticmethod
    def get_app_bar_height(page):
        # Get the height of the page and calculate a dynamic height for the AppBar
        window_height = page.window.height
        window_width = page.window.width

        # Example calculation: Adjust height based on the window size and device orientation
        if window_width > window_height:
            # Landscape mode
            return window_height * 0.15  # 15% of the window height
        else:
            # Portrait mode
            return window_height * 0.005  # 0.5% of the window height

    @staticmethod
    def get_keyboard_height(page):
        return 0  # Not available in Flet

    @staticmethod
    async def is_keyboard_visible(page):
        return False  # No direct equivalent in Flet

    @staticmethod
    async def is_physical_device():
        # Python's platform module can differentiate OS, but not physical vs emulator.
        return platform.system() in ['Linux', 'Darwin', 'Windows']

    @staticmethod
    async def vibrate(duration):
        # No direct method for vibration in Flet.
        pass

    @staticmethod
    async def set_preferred_orientations(orientations):
        # Not available in Flet.
        pass

    @staticmethod
    def hide_status_bar():
        # Not directly supported in Flet.
        pass

    @staticmethod
    def show_status_bar():
        # Not directly supported in Flet.
        pass

    @staticmethod
    async def has_internet_connection():
        try:
            socket.setdefaulttimeout(1)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            return True
        except OSError:
            return False

    @staticmethod
    def is_ios():
        return platform.system() == 'Darwin'

    @staticmethod
    def is_android():
        return platform.system() == 'Linux'

    @staticmethod
    async def launch_url(url):
        webbrowser.open(url)
