
import flet as ft
from pages.home_page import Home
from pages.sign_up import Sign_up
from pages.login import Login
from pages.dashboard import Dashboard

# Define constants for routes
ROUTE_HOME = "/"
ROUTE_SIGNUP = "/signup"
ROUTE_LOGIN = "/login"
ROUTE_DASHBOARD = "/dashboard"
ROUTE_ADMIN  = '/admin'

def main(page: ft.Page):
    
    def route_change(route):
        """Handle route changes."""
        print(f"Routing to {route}")
        page.views.clear()

        if route == ROUTE_HOME:
            view = Home(app=page, route_change=route_change, page=page)
        elif route == ROUTE_SIGNUP:
            view = Sign_up(app=page, route_change=route_change, page=page)
        elif route == ROUTE_LOGIN:
            view = Login(app=page, route_change=route_change, page=page)
        elif route == ROUTE_DASHBOARD:
            view = Dashboard(app=page, route_change=route_change, page=page)
        else:
            view = None  # You can add a 404 or default view here

        if view:
            page.views.append(ft.View(route, [view]))

        page.update()

    def view_pop(_):
        """Handle view pop events."""
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)
        page.update()

    def setup_page():
        """Setup initial page properties."""
        page.title = 'Trading System'
        page.window.width = 420
        page.window.height = 1000
        page.window.left = 1470
        page.window.title_bar_hidden = True
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    # Set page properties
    setup_page()

    # Set event handlers
    page.on_route_change = lambda e: route_change(page.route)
    page.on_view_pop = view_pop

    # Navigate to initial route
    route_change(ROUTE_HOME)

if __name__ == "__main__":
    ft.app(main)
