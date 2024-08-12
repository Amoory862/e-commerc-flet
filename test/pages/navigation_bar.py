import flet as ft
from models.database import UserModel
from models.mongo_setup import get_user_model
from helper.ui_helpers import text_error, elevated_button, text_button, text_field, text_corener

class NavigationBar(ft.UserControl):
    
    def __init__(self, app, route_change, page):
        super().__init__()
        self.page = page
        self.app = app
        self.route_change = route_change
        self.usermodel = get_user_model()
        
    def on_home_click(self, e):
        print("Home button clicked")

    def on_search_click(self, e):
        print("Search button clicked")

    def on_profile_click(self, e):
        print("Profile button clicked")

    def build(self):
        # Bottom Navigation Bar
        bottom_navigation = ft.NavigationBar(
            destinations=[
                ft.Container(bgcolor=ft.colors.GREEN),
                ft.Container(bgcolor=ft.colors.BLUE),
                ft.Container(bgcolor=ft.colors.DEEP_PURPLE),
                ft.Container(bgcolor=ft.colors.ORANGE),
            ]
        )
    

        return bottom_navigation

    
