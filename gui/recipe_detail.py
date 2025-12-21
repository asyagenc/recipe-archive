import customtkinter as ctk

import database
from texts import texts
import manage_recipes
import edit_recipe


def show_recipe_screen(parent_frame, recipe_name, language="en"):
    lang = language

    # Clear screen
    for widget in parent_frame.winfo_children():
        widget.destroy()

    recipe = database.get_recipe_by_name(recipe_name)
    if not recipe:
        return

    (
        name,
        category,
        collection,
        ingredients,
        instructions,
        cooking_time,
        portion,
        notes
    ) = recipe

    container = ctk.CTkFrame(parent_frame)
    container.pack(fill="both", expand=True, padx=30, pady=30)

    # -------------------------
    # HEADER
    # -------------------------
    ctk.CTkLabel(
        container,
        text=name,
        font=ctk.CTkFont(size=26, weight="bold")
    ).pack(anchor="w", pady=(0, 20))

    # -------------------------
    # INFO ROW
    # -------------------------
    info_row = ctk.CTkFrame(container, fg_color="transparent")
    info_row.pack(fill="x", pady=(0, 30))

    info_chip(info_row, texts[lang]["category_label"], category).pack(side="left", padx=5)
    info_chip(info_row, texts[lang]["portion_label"], portion).pack(side="left", padx=5)
    info_chip(
        info_row,
        texts[lang]["cooking_time_label"],
        f"{cooking_time // 60}h {cooking_time % 60}m"
    ).pack(side="left", padx=5)

    # -------------------------
    # CONTENT
    # -------------------------
    content = ctk.CTkFrame(container)
    content.pack(fill="both", expand=True)

    # Ingredients
    left = ctk.CTkFrame(content)
    left.pack(side="left", fill="both", expand=True, padx=(0, 10))

    ctk.CTkLabel(
        left,
        text=texts[lang]["ingredients_label"],
        font=ctk.CTkFont(size=18, weight="bold")
    ).pack(anchor="w", padx=15, pady=(15, 5))

    ingredients_box = ctk.CTkTextbox(left)
    ingredients_box.insert("1.0", ingredients)
    ingredients_box.configure(state="disabled")
    ingredients_box.pack(fill="both", expand=True, padx=15, pady=10)

    # Directions
    right = ctk.CTkFrame(content)
    right.pack(side="left", fill="both", expand=True, padx=(10, 0))

    ctk.CTkLabel(
        right,
        text=texts[lang]["directions_label"],
        font=ctk.CTkFont(size=18, weight="bold")
    ).pack(anchor="w", padx=15, pady=(15, 5))

    directions_box = ctk.CTkTextbox(right)
    directions_box.insert("1.0", instructions)
    directions_box.configure(state="disabled")
    directions_box.pack(fill="both", expand=True, padx=15, pady=10)

    # -------------------------
    # ACTIONS
    # -------------------------
    actions = ctk.CTkFrame(container, fg_color="transparent")
    actions.pack(fill="x", pady=20)

    ctk.CTkButton(
        actions,
        text="← Back",
        width=120,
        command=lambda: manage_recipes.show_manage_recipe_screen(parent_frame, lang)
    ).pack(side="left")

    ctk.CTkButton(
        actions,
        text="Edit",
        width=120,
        command=lambda: edit_recipe.show_edit_recipe_screen(parent_frame, name, lang)
    ).pack(side="right")


def info_chip(parent, label, value, icon=""):
    card = ctk.CTkFrame(
        parent,
        width=180,
        height=90,
        corner_radius=14
    )
    card.pack_propagate(False)

    inner = ctk.CTkFrame(card, fg_color="transparent")
    inner.pack(fill="both", expand=True, padx=12, pady=12)

    if icon:
        ctk.CTkLabel(
            inner,
            text=icon,
            font=ctk.CTkFont(size=20)
        ).pack(anchor="w")

    ctk.CTkLabel(
        inner,
        text=label,
        font=ctk.CTkFont(size=12)
    ).pack(anchor="w", pady=(2, 0))

    ctk.CTkLabel(
        inner,
        text=str(value),
        font=ctk.CTkFont(size=18, weight="bold")
    ).pack(anchor="w")

    return card

