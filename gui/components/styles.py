from tkinter import ttk


def setup_styles():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Card.TFrame",
        background="#f8f9fa",
        relief="raised",
        borderwidth=1
    )

    style.configure(
        "Title.TLabel",
        font=("Segoe UI", 22, "bold"),
        background="#ffffff",
        foreground="#2c3e50"
    )

    style.configure(
        "Subtitle.TLabel",
        font=("Segoe UI", 14, "bold"),
        background="#f8f9fa",
        foreground="#34495e"
    )

    style.configure(
        "Stat.TLabel",
        font=("Segoe UI", 16, "bold"),
        background="#f8f9fa",
        foreground="#2c3e50"
    )

    style.configure(
        "Menu.TButton",
        font=("Segoe UI", 11),
        padding=10
    )
