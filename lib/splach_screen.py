import flet as ft
from lib.utils.constants.image_strings import TImages
from lib.utils.theme.theme import AppTheme
import asyncio
from lib.utils.helpers.get_theme_from_device import ThemeProviderCustom
theme_provider = AppTheme()

class SplashScreen(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(self)
        self.page = page 
        #self.page.theme_mode = ft.ThemeMode.SYSTEM
        # self.page.theme = theme_provider.light_theme
        # self.page.dark_theme = theme_provider.dark_theme 
        #self.page.window.width = 480
        #self.page.window.height = 1000
        #self.page.window.left = 1450
        self.page.theme_mode = ThemeProviderCustom.get_actual_theme(self,page)

    def build(self):
    # Determine the current theme mode by checking if the light or dark theme is applied
    
        if self.page.theme_mode == 'light' :
            logo = TImages.dark_app_logo
            bgcolor = ft.colors.WHITE
        elif self.page.theme_mode == 'dark' :
            logo = TImages.light_app_logo
            bgcolor = ft.colors.BLACK
        elif self.page.theme_mode == 'system':
            print('your use a system theme ')
            

            
        # Create the splash screen UI
        splash_screen = ft.Container(
            content=ft.Image(src=logo, 
                             width=250, height=250,border_radius=ft.border_radius.all(50),fit=ft.ImageFit.CONTAIN), 
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=bgcolor,
            width=self.page.window.width,
            height=self.page.window.height,
        )
        return splash_screen

    async def show(self):
        # Add the splash screen to the page and update
        self.page.add(self.build())
        self.page.update()

        # Delay before moving to the main content
        await asyncio.sleep(.5) 
        self.page.remove(self.page.controls[0])
        self.page.update()

# async def main(page:ft.Page):
    
#     #page.theme_mode = ft.ThemeMode.SYSTEM
#     if page.theme_mode == ft.ThemeMode.LIGHT.value:
#         page.theme = theme_provider.light_theme
#         page.bgcolor = '#ffffffff'
#     elif page.theme_mode == ft.ThemeMode.DARK.value:
#         page.bgcolor = '#0000000'
#         page.dark_theme = theme_provider.dark_theme
#     else:
#         page.theme_mode == ft.ThemeMode.SYSTEM.value
    
#      # Show the splash screen
#     splash = SplashScreen(page)
#     await splash.show()  # Await the splash screen's show method
    
# ft.app(main)