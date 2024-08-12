import flet as ft
 

class TColors:
    # App theme colors
    primary = "#4b68ff"  # Hexadecimal color code
    secondary = "#FFE24B"
    accent = "#b0c7ff"
    
    # Gradient Colors
    gradient = ft.LinearGradient(
        begin=ft.Alignment(0.0,0.0),
        end=ft.Alignment(0.707,-0.707),
        colors=[
            '#DB9696',
            '#AACD9D',
            '#A4C4C2'
        ]
    )

    # Text colors
    textPrimary = "#333333"
    textSecondary = "#6C757D"
    textWhite = "#FFFFFF"

    # Background colors
    light = "#F6F6F6"
    dark = "#272727"
    primaryBackground = "#F3F5FF"

    # Background Container colors
    lightContainer = "#F6F6F6"
    darkContainer = "#FFFFFF"  # Adjust opacity with the method available in Flet, if any

    # Button colors
    buttonPrimary = "#4b68ff"
    buttonSecondary = "#6C757D"
    buttonDisabled = "#C4C4C4"

    # Border colors
    borderPrimary = "#D9D9D9"
    borderSecondary = "#E6E6E6"

    # Error and validation colors
    error = "#D32F2F"
    success = "#388E3C"
    warning = "#F57C00"
    info = "#1976D2"

    # Neutral Shades
    black = "#232323"
    darkerGrey = "#4F4F4F"
    darkGrey = "#939393"
    grey = "#E0E0E0"
    softGrey = "#F4F4F4"
    lightGrey = "#F9F9F9"
    white = "#FFFFFF"
    _black = '#000000'
    _gey = '#424242'


