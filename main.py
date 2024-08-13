import flet as ft
from lib.utils.theme.theme import AppTheme
from lib.utils.constants.text_strings import TTexts
from lib.splach_screen import SplashScreen 
from lib.utils.helpers.get_theme_from_device import ThemeProviderCustom 
from lib.features.authentication.pages.onboading.onboarding import OnBoardingScreen 
#--------------------------------------------# 
#  TODO  add splach scren [done]             #    
#  TODO  add onboarding screen  23.42        #   
#  TODO  add login page 16.45                #
#  TODO  add signup page 17.12               #
#  TODO  add email vervication screen 16.38  #
#  TODO  add forgot password screen 10.19    # 
#  TODO  add navigation bar 15.45            # 
#  TODO  clip path 27.49                     #
#  TODO  cistom appbar 17.06                 #
#  TODO  add search bar and list view 28.29  #
#--------------------------------------------#

 
class App:
    @staticmethod
    async def main(page: ft.Page):
        # Set window title and display settings
        page.title = TTexts.appName
        page.window.width = 480
        page.window.height = 1000
        page.window.left = 1437 
        page.update()
        # Create an instance of AppTheme
        theme_provider = AppTheme()
        
        # Create an instance of ThemeProviderCustom to determine the theme
        theme_provider_custom = ThemeProviderCustom()
        
        # Update the page to apply initial settings
        page.update()
        
        # Set the theme mode based on system preference
        page.theme_mode = theme_provider_custom.get_actual_theme(page)
        page.update()
        
        # Apply the determined theme
        theme_provider_custom.apply_theme(page, page.theme_mode)
        page.update()
        
        # Get the actual theme
        actual_theme = theme_provider_custom.get_actual_theme(page)
        page.update()
        page.theme_mode = actual_theme
        
        # Set background and theme based on the actual theme
        if page.theme_mode == ft.ThemeMode.DARK.value:
            page.bgcolor = '#000000'
            page.theme = theme_provider.dark_theme
            page.update()
        elif page.theme_mode == ft.ThemeMode.LIGHT.value:
            page.bgcolor = '#FFFFFF'
            page.theme = theme_provider.light_theme
            page.update()
        else:
            print('Unhandled theme mode')
        
        # Update the page after setting the theme
        page.update()
        
        # Show the splash screen 
        splash = SplashScreen(page)
        await splash.show()  # Wait until the splash screen is shown 
        
        #Show onboaeding screen 
        onboarding_screen = OnBoardingScreen(page)
        page.add(onboarding_screen)


# Run the application
# if '__main__'==__name__:
ft.app(target=App.main)
