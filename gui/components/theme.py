import customtkinter as ctk

THEMES = {
    "light": {
        "mode": "light",
        "accent": "#3B82F6"
    },
    "dark": {
        "mode": "dark",
        "accent": "#3B82F6"
    }
}

current_theme = "light"


def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name

    ctk.set_appearance_mode(THEMES[theme_name]["mode"])
    ctk.set_default_color_theme("blue")  # base theme


def get_theme():
    return current_theme
