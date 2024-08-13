import flet  as ft
from lib.utils.constants.text_strings import TTexts
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes
from lib.utils.device.device_utility import TDeviceUtils
from lib.custom_lib.SmoothPageIndicatorFlet.ExpandingDotsEffect import ExpandingDotsEffect
from lib.custom_lib.SmoothPageIndicatorFlet.SmoothPageIndicator import SmoothPageIndicator
from lib.utils.helpers.get_theme_from_device import ThemeProviderCustom

class CircularButton(ft.UserControl):
    def __init__(self,page:ft.Page) -> None:
        super().__init__()
        self.page = page
        self.current_page = 0
        self.page.theme_mode = ThemeProviderCustom.get_actual_theme(self,self.page)
        
    def build(self):
        return ft.Stack(
                    controls=[
                        ft.Column(
                                right=TSizes.default_space,
                                bottom=TDeviceUtils.get_bottom_navigation_bar_height()+35,
                                controls=[
                                          ft.ElevatedButton(
                                              on_click=...,
                                              style=ft.ButtonStyle(shape=ft.CircleBorder(),bgcolor=ft.colors.BLACK if self.page.theme_mode == 'light' else TColors.primary),
                                              content=ft.Icon(name=ft.icons.ARROW_RIGHT_ALT_SHARP,size=45,color=TColors.white if self.page.theme_mode == 'light' else TColors.black,), 
                                          )
                                          ],
                                    
                                )
                    ]
                )
