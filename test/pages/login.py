
import flet as ft
from models.mongo_setup import get_user_model
from helper.ui_helpers import text_error, elevated_button, text_button, text_field,text_corener

class Login(ft.UserControl):
    
    def __init__(self, app, route_change, page):
        super().__init__()
        self.page = page
        self.app = app
        self.route_change = route_change
        self.usermodel = get_user_model()
        
    def login(self, e):
        username = self.username_field.value
        password = self.password_field.value

        if not username or not  password :
            self.error_text.value = "All fields are required!"
            self.update()
            return
        
        user = self.usermodel.find_user(username) 
        
        if user and user.get('password') == password:
            self.error_text.value = "Login successful!"
            print("Login successful!")
            self.update()
            self.route_change("/dashboard")  # Redirect to a dashboard page
            
        else:
            self.error_text.value = 'Invalid username or password.'
            print("Invalid username or password.")
            self.update()
            
    def navigate_to_signup(self, e):
        self.route_change("/signup")
        self.update()
        
    def build(self):
        self.log_text = text_corener('Log In')
        self.username_field = text_field("Username")
        self.password_field = text_field("Password", pass_=True, show_pass=True)
        self.error_text = text_error()

        return ft.Container(
            width=440,
            height=975,
            border_radius=30,
            padding=20,
            border=ft.border.all(2,'black'),
            content=ft.ResponsiveRow(
                controls=[
                    self.log_text,
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            ft.Image(src='.//assets/1.gif', border_radius=15, scale=0.75),
                            ft.Container(height=10),
                            self.username_field,
                            self.password_field,
                            self.error_text,
                            elevated_button(
                                text="Log In",
                                fun=self.login
                            ),
                            text_button(
                                text="Don't have an account? Sign Up",
                                fun=self.navigate_to_signup
                            )
                        ]
                    )
                ]
            )
        )

    

