# ft.RoundedRectangleBorder(radius=12)


# padding=ft.EdgeInsets.symmetric(vertical=12), =ft.padding.symmetric(vertical=12, horizontal=12)






# "#80000000"
# "#80F6F6F6"




# import flet as ft

# def main(page: ft.Page):
#     # Set your custom theme mode to SYSTEM
#     page.theme_mode = ft.ThemeMode.SYSTEM
    
#     # Function to determine the actual theme mode
#     def get_current_theme_mode():
#         return page.theme_mode if page.theme_mode != ft.ThemeMode.SYSTEM else (page.theme == page.theme_provider.dark_theme and ft.ThemeMode.DARK or ft.ThemeMode.LIGHT)
    
#     current_theme_mode = get_current_theme_mode()
    
#     # Print the current theme mode
#     print(f"Current theme mode: {current_theme_mode}")

#     # Set up UI elements based on theme
#     if current_theme_mode == ft.ThemeMode.DARK:
#         page.controls.append(ft.Text("Dark mode is active"))
#     else:
#         page.controls.append(ft.Text("Light mode is active"))

#     # Add other UI elements or logic here
#     page.update()

# ft.app(target=main)
# 
# 
# 
# 
# 

import flet as ft

# import flet as ft

# class CustomTheme:
#     def __init__(self, primary_color: str, background_color: str):
#         self.primary_color = primary_color
#         self.background_color = background_color

#     def to_flet_theme(self) -> ft.Theme:
#         return ft.Theme(
#             primary_color=self.primary_color,
#             # Add more Flet theme attributes as needed
#         )

# class ThemeProvider:
#     def __init__(self):
#         # Define light and dark themes similar to Flutter's ThemeData
#         self.light_theme = CustomTheme(
#             primary_color="blue",
#             background_color="white"
#         )
#         self.dark_theme = CustomTheme(
#             primary_color="orange",
#             background_color="black"
#         )

#     def apply_system_theme(self, page: ft.Page):
#         # Mimic system theme detection
#         brightness = page.platform_brightness  # Simulates getting system brightness

#         if brightness == ft.Brightness.DARK:
#             page.theme = self.dark_theme.to_flet_theme()
#         else:
#             page.theme = self.light_theme.to_flet_theme()

#         page.update()

#     def apply_theme(self, page: ft.Page, theme_mode: ft.ThemeMode):
#         # Apply the correct theme based on the theme_mode
#         if theme_mode == ft.ThemeMode.DARK:
#             page.theme = self.dark_theme.to_flet_theme()
#         elif theme_mode == ft.ThemeMode.LIGHT:
#             page.theme = self.light_theme.to_flet_theme()
#         else:  # SYSTEM
#             self.apply_system_theme(page)

# def main(page: ft.Page):
#     theme_provider = ThemeProvider()

#     # Set theme mode to SYSTEM to mimic Flutter's behavior
#     page.theme_mode = ft.ThemeMode.SYSTEM
    
#     # Apply the theme based on the current theme_mode
#     theme_provider.apply_theme(page, page.theme_mode)

#     # Update the page to ensure the theme is applied
#     page.update()

#     # Display the current theme mode
#     dark_mode_active = page.theme.primary_color == theme_provider.dark_theme.primary_color
#     page.controls.append(ft.Text(
#         "Dark mode is active" if dark_mode_active else "Light mode is active",
#         size=24
#     ))

#     page.update()

# ft.app(target=main)



'''
return ft.Container( # Horizonal Scrollable Pages
                
            content=ft.Row(
                controls=[
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
                scroll=ft.ScrollMode.HIDDEN
                #clip_behavior=ft.ClipBehavior.HARD_EDGE 
            )
            )
'''


''''
return ft.UserControl(
            controls=[
                ft.Stack(
                    [
                        ft.Row(
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
                            scroll=ft.ScrollMode.ALWAYS,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    
                )
            ],
            height=THelperFunctions.screen_height(self.page) ,
            width=THelperFunctions.screen_width(self.page),
            
        )
'''
import flet as ft
from lib.utils.constants.image_strings import TImages
# def main(page: ft.Page):
#         st = ft.Stack(
#             controls=[
#                 ft.Image(
#                     src=TImages.banner2,
#                     width=300,
#                     height=300,
#                     fit=ft.ImageFit.CONTAIN,
#                 ),
#                 ft.Row(
#                     controls=[
#                         ft.Text(
#                             "Image title",
#                             color="white",
#                             size=40,
#                             weight="bold",
#                             opacity=0.5,
#                         ),
#                         ft.Image(
#                     src=TImages.banner2,
#                     width=300,
#                     height=300,
#                     fit=ft.ImageFit.CONTAIN,
#                 ),
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,
#                 ),
#             ],
#             width=300,
#             height=300,
#         )

#         page.add(st)

# ft.app(target=main)
# 
# from time import sleep
# import flet as ft

# def main(page: ft.Page):
#     page.title = "Auto-scrolling ListView"

#     lv = ft.ListView(expand=1, spacing=3, padding=20, auto_scroll=False)

#     count = 1

#     for i in range(0, 60):
#         lv.controls.append(ft.Text(f"Line {count}"))
#         count += 1

#     page.add(lv)

#     for i in range(0, 60):
#         sleep(1)
#         lv.controls.append(ft.Text(f"Line {count}"))
#         count += 1
#         page.update()

# ft.app(target=main)



