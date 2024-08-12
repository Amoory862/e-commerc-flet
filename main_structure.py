
import flet as ft
from models.database import UserModel
from models.mongo_setup import get_user_model
from helper.ui_helpers import text_error, elevated_button, text_button, text_field,text_corener

class Main(ft.UserControl):
    
    def __init__(self, app, route_change, page):
        super().__init__()
        self.page = page
        self.app = app
        self.route_change = route_change
        self.usermodel = get_user_model()
        
    # Define your functions here
    # Example:
    # def some_function(self, e):
    #     pass

    def navigate_to_another_page(self, e):
        self.route_change(self.app, "/another_page")  # Replace with your route


    def build(self):
        self.title_text = text_corener()
        
        self.error_text = text_error()

        # Add your widgets here
        # Example:
        # self.username_field = text_field("Username")
        # self.email_field = text_field("Email")
        # self.image = ft.Image(src='.//assets/1.gif', border_radius=15, scale=0.75)

        return ft.Container(
            width=440,
            height=975,
            padding=20,
            border_radius=30,
            border=ft.border.all(2,'black'),
            content=ft.ResponsiveRow(
                controls=[
                    self.title_text,
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            # Add your widgets to this column
                            # self.username_field,
                            # self.email_field,
                            # self.image,
                            self.error_text,
                            elevated_button(
                                text="Button Text",  # Replace with your button text
                                fun=self.some_function  # Replace with your function
                            ),
                            text_button(
                                text="Text Button",  # Replace with your text button
                                fun=self.some_function  # Replace with your function
                            )
                        ]
                    )
                ]
            )
        )

    
