import flet as ft

class ExpandingDotsEffect:
    def __init__(
        self,
        expansion_factor: float = 5.0,
        dot_width: float = 10.0,
        dot_height: float = 6.0,
        spacing: float = 1.0,
        radius: float = 16.0,
        active_dot_color: str = "indigo",
        dot_color: str = "grey"
    ):
        assert expansion_factor > 1, "Expansion factor must be greater than 1"
        self.expansion_factor = expansion_factor
        self.dot_width = dot_width
        self.dot_height = dot_height
        self.spacing = spacing
        self.radius = radius
        self.active_dot_color = active_dot_color
        self.dot_color = dot_color

    def calculate_size(self, count: int):
        return ((self.dot_width + self.spacing) * (count - 1)) + (self.expansion_factor * self.dot_width), self.dot_height
