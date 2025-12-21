import customtkinter as ctk
import database
import recipe_detail
from texts import texts

def stat_card(parent, title, value):
    card = ctk.CTkFrame(parent, width=200, height=100)
    card.pack_propagate(False)

    ctk.CTkLabel(
        card,
        text=title,
        font=ctk.CTkFont(size=14, weight="bold")
    ).pack(anchor="w", padx=15, pady=(15, 5))

    ctk.CTkLabel(
        card,
        text=str(value),
        font=ctk.CTkFont(size=22, weight="bold")
    ).pack(anchor="w", padx=15)

    return card



def show_dashboard(parent_frame, language):
    lang = language

    for widget in parent_frame.winfo_children():
        widget.destroy()

    container = ctk.CTkFrame(parent_frame)
    container.pack(fill="both", expand=True, padx=30, pady=30)

    # Header
    ctk.CTkLabel(
        container,
        text=texts[lang]["dashboard_greeting"],
        font=ctk.CTkFont(size=24, weight="bold")
    ).pack(anchor="w", pady=(0, 30))

    # Stats row
    stats_row = ctk.CTkFrame(container, fg_color="transparent")
    stats_row.pack(fill="x", pady=(0, 30))

    total_recipes = database.get_total_recipe_count()

    stat_card(stats_row, "🍽 Total Recipes", total_recipes).pack(side="left", padx=10)
    stat_card(stats_row, "📂 Categories", "Soon").pack(side="left", padx=10)

    # Recent
    ctk.CTkLabel(
        container,
        text="🕒 Recently Added",
        font=ctk.CTkFont(size=18, weight="bold")
    ).pack(anchor="w", pady=(0, 10))

    for recipe in database.get_latest_recipes(6):
        ctk.CTkButton(
            container,
            text=recipe,
            height=40,
            corner_radius=10,
            anchor="w",
            command=lambda r=recipe:
                recipe_detail.show_recipe_screen(parent_frame, r, lang)
        ).pack(fill="x", pady=6)
