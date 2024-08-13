import flet as ft
from lib.utils.constants.image_strings import TImages
from lib.utils.constants.text_strings import TTexts
from lib.utils.constants.sizes import TSizes
from lib.utils.helpers.helper_functions import THelperFunctions
from lib.utils.device.device_utility import TDeviceUtils

class AppBarStack(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        # Define the TextButton and Stack layout
        return ft.Stack(
            controls=[
                ft.TextButton(
                    top=TDeviceUtils.get_app_bar_height(page=self.page),
                    right=TSizes.default_space,
                    text='Skip',
                    on_click=...
                ),
            ],
        )