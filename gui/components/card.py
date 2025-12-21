import tkinter as tk
from tkinter import ttk


class InfoCard(ttk.Frame):
    def __init__(self, parent, title, value, width=200):
        super().__init__(parent, style="Card.TFrame", padding=20)

        self.configure(width=width)
        self.pack_propagate(False)

        ttk.Label(
            self,
            text=title,
            style="Subtitle.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            self,
            text=value,
            style="Stat.TLabel"
        ).pack(anchor="w", pady=(10, 0))
