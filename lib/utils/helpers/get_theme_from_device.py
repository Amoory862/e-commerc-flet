import flet as ft

class CustomTheme:
    def __init__(self, primary_color: str, background_color: str):
        self.primary_color = primary_color
        self.background_color = background_color

    def to_flet_theme(self) -> ft.Theme:
        return ft.Theme(
            primary_color=self.primary_color,
            # Add more Flet theme attributes as needed
        )

class ThemeProviderCustom:
    def __init__(self):
        # Define light and dark themes similar to Flutter's ThemeData
        self.light_theme = CustomTheme(
            primary_color="blue",
            background_color="white"
        )
        self.dark_theme = CustomTheme(
            primary_color="orange",
            background_color="black"
        )

    def get_actual_theme(self, page: ft.Page) -> str:
        # Mimic system theme detection
        brightness = page.platform_brightness  # Simulates getting system brightness

        if brightness == ft.Brightness.DARK:
            return "dark"
        elif brightness == ft.Brightness.LIGHT:
            return "light"
        else:
            return 'system'

    def apply_system_theme(self, page: ft.Page):
        actual_theme = self.get_actual_theme(page)
        if actual_theme == "dark":
            page.theme = self.dark_theme.to_flet_theme()
        else:
            page.theme = self.light_theme.to_flet_theme()

        page.update()

    def apply_theme(self, page: ft.Page, theme_mode: ft.ThemeMode):
        # Apply the correct theme based on the theme_mode
        if theme_mode == ft.ThemeMode.DARK:
            page.theme = self.dark_theme.to_flet_theme()
        elif theme_mode == ft.ThemeMode.LIGHT:
            page.theme = self.light_theme.to_flet_theme()
        else:  # SYSTEM
            self.apply_system_theme(page)

def main(page: ft.Page):
    theme_provider = ThemeProviderCustom()

    # Set theme mode to SYSTEM to mimic Flutter's behavior
    page.theme_mode = ft.ThemeMode.SYSTEM
    
    # Apply the theme based on the current theme_mode
    theme_provider.apply_theme(page, page.theme_mode)

    # Update the page to ensure the theme is applied
    page.update()
    
    # Display the current theme mode
    actual_theme = theme_provider.get_actual_theme(page)
    page.controls.append(ft.Text(
        f"The current theme is {actual_theme}",
        size=24
    ))
    print(f"The actual theme mode is: {actual_theme}")
    page.update()
    return actual_theme

# Run the application
#ft.app(target=main)
