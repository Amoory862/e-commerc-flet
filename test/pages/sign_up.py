
import re
import flet as ft
from models.database import UserModel
from models.mongo_setup import get_user_model
from helper.ui_helpers import text_error, elevated_button, text_button, text_field,text_corener

# add this
class Sign_up(ft.UserControl):
    
    def __init__(self, app, route_change, page):
        super().__init__()
        self.page = page
        self.app = app
        self.route_change = route_change
        self.usermodel = get_user_model()
        
    def signup(self, e):
        username = self.username_field.value.strip()
        email = self.email_field.value.strip()
        password = self.password_field.value.strip()
        confirm_password = self.confirm_password_field.value.strip()

        if not username or not email or not password or not confirm_password:
            self.error_text.value = "All fields are required!"
            self.update()
            return

        if len(username) < 5 or len(username) > 20:
            self.error_text.value = "Username must be between 5 and 20 characters!"
            self.update()
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.error_text.value = "Invalid email address!"
            self.update()
            return

        if password != confirm_password:
            self.error_text.value = "Passwords do not match!"
            self.update()
            return

        if len(password) < 8:
            self.error_text.value = "Password must be at least 8 characters long!"
            self.update()
            return

        self.usermodel.add_user(username, email, password)
        self.error_text.value = "User registered successfully!"
        print("User registered successfully!")
        self.update()
        self.route_change("/login")

    def navigate_to_login(self, e):
        self.route_change("/login")

    def build(self):
        self.reg_text = text_corener('Sign Up')
        self.error_text = text_error()
        self.username_field = text_field("Username")
        self.email_field = text_field("Email")
        self.password_field = text_field("Password", pass_=True, show_pass=True)
        self.confirm_password_field = text_field("Confirm Password", pass_=True, show_pass=True)

        
        # add this Container with all thing and add comment to wher i can add my widget image, text filed,button
        
        return ft.Container(
            width=440,
            height=975,
            padding=20,
            border_radius=30,
            border=ft.border.all(2,'black'), 
            content=ft.ResponsiveRow(
                controls=[
                    self.reg_text,
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.Image(src='.//assets/1.gif', border_radius=15, scale=0.75),
                            ft.Container(height=10),
                            self.username_field,
                            self.email_field,
                            self.password_field,
                            self.confirm_password_field,
                            self.error_text,
                            elevated_button(
                                text="Sign Up", 
                                fun=self.signup
                            ),
                            text_button(
                                text="Already have an account? Login",
                                fun=self.navigate_to_login
                            )
                        ]
                    )
                ]
            )
        )

    

