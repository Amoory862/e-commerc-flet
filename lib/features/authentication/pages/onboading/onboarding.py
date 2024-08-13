import flet as ft
from lib.utils.constants.image_strings import TImages
from lib.utils.constants.text_strings import TTexts
from lib.utils.helpers.helper_functions import THelperFunctions
from lib.features.authentication.pages.onboading.widgets.onboarding_page import OnBoardingPage
from lib.features.authentication.pages.onboading.widgets.onboarding_skip import AppBarStack
from lib.custom_lib.SmoothPageIndicatorFlet.SmoothPageIndicator  import SmoothPageIndicator
from lib.utils.helpers.get_theme_from_device import ThemeProviderCustom
from lib.features.authentication.pages.onboading.widgets.onboarding_dot_navi import DotNavi
from lib.features.authentication.pages.onboading.widgets.circular_button import CircularButton

class OnBoardingScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.current_page = 0
        self.page.theme_mode = ThemeProviderCustom.get_actual_theme(self,self.page)

    def navigate_to_another_page(self, e):
        self.route_change(self.app, "/another_page")  # Replace with your route
        
    def build(self):
        current_theme = self.page.theme
        # print(self.page.theme_mode=='dark')
        return ft.UserControl(
            controls=[
                    # Horizontal Scrollable Pages
                    ft.ListView(
                        [
                        OnBoardingPage(
                            self.page,
                            image=TImages.on_boarding_image1,
                            title=TTexts.onBoardingTitle1,
                            subtitle=TTexts.onBoardingSubTitle1
                        ),
                        OnBoardingPage(
                            self.page,
                            image=TImages.on_boarding_image2,  
                            title=TTexts.onBoardingTitle2,     
                            subtitle=TTexts.onBoardingSubTitle2 
                        ),
                        OnBoardingPage(
                            self.page,
                            image=TImages.on_boarding_image3,  
                            title=TTexts.onBoardingTitle3,     
                            subtitle=TTexts.onBoardingSubTitle3 
                        )
                        ], 
                        # scroll=ft.ScrollMode.ALWAYS,
                        # alignment=ft.MainAxisAlignment.START,
                        # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        horizontal=True,
                        expand=True,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,  # Clip content if it overflows
                        
                    ),
                    # Skip Button
                    AppBarStack(page=self.page),
                    # Add the indicator and button to the page 
                    DotNavi(page=self.page),
                    # Circular Button 
                    CircularButton(page=self.page)
                
            ],
            height=THelperFunctions.screen_height(self.page),
            width=THelperFunctions.screen_width(self.page),
        )
            

                