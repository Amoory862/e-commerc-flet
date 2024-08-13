from.ExpandingDotsEffect import ExpandingDotsEffect 
import flet as ft


class SmoothPageIndicator(ft.UserControl):
    def __init__(self, count: int, effect: ExpandingDotsEffect = None):
        super().__init__()
        self.count = count
        self.effect = effect if effect is not None else ExpandingDotsEffect()
        self.current_page = 0  
        
    def update_dots(self, current_page):
        self.current_page = current_page
        self.update()

    def build(self):
        dots = [
            ft.Container(
                width=self.effect.dot_width * self.effect.expansion_factor if i == self.current_page else self.effect.dot_width,
                height=self.effect.dot_height,
                bgcolor=self.effect.active_dot_color if i == self.current_page else self.effect.dot_color,
                border_radius=ft.border_radius.all(self.effect.radius),
                margin=ft.Margin(4, 0, 4, 0)
            ) for i in range(self.count)
        ]

        return ft.Row(
            controls=dots,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    


