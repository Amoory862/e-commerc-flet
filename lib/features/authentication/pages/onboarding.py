import flet as ft
from lib.utils.constants.image_strings import TImages
from lib.utils.constants.text_strings import TTexts
from lib.utils.constants.sizes import TSizes
from lib.utils.helpers.helper_functions import THelperFunctions

class OnBoardingScreen(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def navigate_to_another_page(self, e):
        self.route_change(self.app, "/another_page")  # Replace with your route

    def build(self):
        return ft.UserControl(
            controls=[
                ft.Stack(
                    [
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
                            expand=1,
                            spacing=2,

                        )
                    ],
                )
            ],
            height=THelperFunctions.screen_height(self.page),
            width=THelperFunctions.screen_width(self.page),
        )
            
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
                        
                    ),
                    ft.Text(height=TSizes.space_btw_items),  
                    ft.Text(
                        self.subtitle,
                        style=current_theme.text_theme.body_medium,
                        text_align=ft.TextAlign.CENTER,
                        width=THelperFunctions.screen_width(self.page)*0.7,
                        height=THelperFunctions.screen_height(self.page) 
                    ),
                    
            ],
            
        ),
        padding=ft.padding.all(TSizes.default_space)  # Add padding here
    )
                
                
        
            
