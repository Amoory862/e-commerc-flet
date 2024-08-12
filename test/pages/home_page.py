
import flet as ft
from helper.ui_helpers import elevated_button,text_button,text_corener,main_text


class Home(ft.UserControl):
    
    def __init__(self, app, route_change, page):
        super().__init__()
        self.page = page
        self.app = app
        self.route_change = route_change

        
    def navigate_to_sign_up(self, e):
        self.route_change("/signup")

    def navigate_to_login(self, e):
        self.route_change("/login")  
        

    def build(self):
        self.app_text = text_corener('MT5 Trading Bot')
        self.start_text = main_text('Welcome To Our App')
        self.sign_up_btn = elevated_button(text="Sign Up",
                                fun=self.navigate_to_sign_up)
        self.already_btn = text_button(text="Already have an account? Login",
                                fun=self.navigate_to_login)


        #main container of app 
        return ft.Container( 
            width=440,
            height=975,
            border_radius=30,
            padding=20,
            border=ft.border.all(2,'black'), 
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        controls=[
                            self.app_text
                            ])
                    ,
                    
                    #column main text with photo 
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=50,
                        controls=[
                            self.start_text,
                            ft.Image(src='.//assets/home.png', border_radius=15, scale=1.15),
                            ft.Container(height=30),  # Add space before the sign-up button
                            
                        ]
                    ),
                    
                    # column sign up and already have an accounnt 
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        
                        controls=[
                            self.sign_up_btn,
                            self.already_btn,

                        ]
                    )
                ]
            )
        )
        

    


    

