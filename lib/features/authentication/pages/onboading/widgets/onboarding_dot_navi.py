import flet  as ft
from lib.utils.constants.text_strings import TTexts
from lib.utils.constants.colors import TColors
from lib.utils.constants.sizes import TSizes
from lib.utils.device.device_utility import TDeviceUtils
from lib.custom_lib.SmoothPageIndicatorFlet.ExpandingDotsEffect import ExpandingDotsEffect
from lib.custom_lib.SmoothPageIndicatorFlet.SmoothPageIndicator import SmoothPageIndicator
from lib.utils.helpers.get_theme_from_device import ThemeProviderCustom

class DotNavi(ft.UserControl):
    def __init__(self,page:ft.Page) -> None:
        super().__init__()
        self.page = page
        self.current_page = 0
        self.page.theme_mode = ThemeProviderCustom.get_actual_theme(self,self.page)
        
    def build(self):
        current_theme = self.page.theme
        print(self.page.theme_mode=='dark')
         # Define the SmoothPageIndicator with ExpandingDotsEffect
        indicator = SmoothPageIndicator(
            count=3,  # Number of pages in OnBoardingPage
            effect=ExpandingDotsEffect(
                active_dot_color=TColors.white if self.page.theme_mode=='dark' else TColors.dark ,  # You can customize these colors
                dot_color=TColors._gey 
            )
        )
        
    
        
        return ft.Stack(
                    controls=[
                        ft.Row(
                                left=TSizes.default_space,
                                bottom=TDeviceUtils.get_bottom_navigation_bar_height() + 55 ,
                                controls=[indicator],
                                    
                                )
                    ]
                )
