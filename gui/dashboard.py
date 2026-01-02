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
    
    # Ana container (sabit)
    container = ctk.CTkFrame(parent_frame, fg_color="transparent")
    container.pack(fill="both", expand=True, padx=30, pady=30)
    
    # Header (sabit)
    ctk.CTkLabel(
        container,
        text=texts[lang]["dashboard_greeting"],
        font=ctk.CTkFont(size=24, weight="bold")
    ).pack(anchor="w", pady=(0, 30))
    
    # Stats row (sabit)
    stats_row = ctk.CTkFrame(container, fg_color="transparent")
    stats_row.pack(fill="x", pady=(0, 30))
    
    total_recipes = database.get_total_recipe_count()
    stat_card(
        stats_row,
        texts[lang]["total_recipes"],
        total_recipes
    ).pack(side="left", padx=10)
    
    category_count = database.get_category_count()
    stat_card(
        stats_row,
        texts[lang]["categories"],
        category_count
    ).pack(side="left", padx=10)
    
    # Recent Recipes Section Header (sabit)
    ctk.CTkLabel(
        container,
        text=texts[lang]["recently_added"],
        font=ctk.CTkFont(size=18, weight="bold")
    ).pack(anchor="w", pady=(0, 10))
    
    # Scrollable frame sadece tarifler için
    scrollable_frame = ctk.CTkScrollableFrame(
        container,
        fg_color="transparent"
    )
    scrollable_frame.pack(fill="both", expand=True)
    
    # Tüm tarifleri göster
    all_recipes = database.get_latest_recipes()
    
    if all_recipes:
        for recipe in all_recipes:
            ctk.CTkButton(
                scrollable_frame,
                text=recipe,
                height=40,
                corner_radius=10,
                anchor="w",
                fg_color="#FF8C00",
                hover_color="#FF7000",
                text_color="white", 
                command=lambda r=recipe: recipe_detail.show_recipe_screen(parent_frame, r, lang)
            ).pack(fill="x", pady=6)
    else:
        ctk.CTkLabel(
            scrollable_frame,
            text=texts[lang].get("no_recipes", "Henüz tarif yok"),
            font=ctk.CTkFont(size=14),
            text_color="gray"
        ).pack(anchor="w", pady=10)