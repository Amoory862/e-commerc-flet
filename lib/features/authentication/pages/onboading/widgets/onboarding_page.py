import flet as ft
from lib.utils.constants.image_strings import TImages
from lib.utils.constants.text_strings import TTexts
from lib.utils.constants.sizes import TSizes
from lib.utils.helpers.helper_functions import THelperFunctions
from lib.utils.device.device_utility import TDeviceUtils

class OnBoardingPage(ft.UserControl):
    def __init__(self, page, image, title, subtitle):
        super().__init__()
        self.page = page
        self.image = image
        self.title = title
        self.subtitle = subtitle

    def build(self):
        current_theme = self.page.theme
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=self.image,
                        width=THelperFunctions.screen_width(self.page) * .8,
                        height=THelperFunctions.screen_height(self.page) * .6
                    ),
                    ft.Text(
                        self.title,
                        style=current_theme.text_theme.headline_medium,
                        text_align=ft.TextAlign.CENTER,
                        width=THelperFunctions.screen_width(self.page)*0.85, 
                        #height=THelperFunctions.screen_height(self.page) 
                        
                    ),
                    ft.Text(height=TSizes.space_btw_items),  
                    ft.Text(
                        self.subtitle,
                        style=current_theme.text_theme.body_medium,
                        text_align=ft.TextAlign.CENTER,
                        width=THelperFunctions.screen_width(self.page)*0.8,
                        # height=THelperFunctions.screen_height(self.page) 
                    ),
                    
            ],
            
        ),
        padding=ft.padding.all(TSizes.default_space),  # Add padding here
        alignment=ft.alignment.center,
    )