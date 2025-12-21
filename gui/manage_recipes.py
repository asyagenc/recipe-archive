import customtkinter as ctk

import edit_recipe
import recipe_detail
import database
from texts import texts


def recipe_list(list_frame, recipes, parent_frame, language):
    lang = language

    for widget in list_frame.winfo_children():
        widget.destroy()

    edit_icon = texts[lang]["edit_icon"]
    delete_icon = texts[lang]["delete_icon"]

    for recipe in recipes:
        row = ctk.CTkFrame(list_frame, height=48)
        row.pack(fill="x", pady=6)
        row.pack_propagate(False)

        # Recipe name (clickable → DETAIL)
        ctk.CTkButton(
            row,
            text=recipe,
            anchor="w",
            fg_color="transparent",
            hover_color="#e8e8e8",
            text_color=("black", "white"),
            command=lambda r=recipe:
                recipe_detail.show_recipe_screen(parent_frame, r, lang)
        ).pack(side="left", fill="x", expand=True, padx=(15, 5))

        # Edit
        ctk.CTkButton(
            row,
            text=edit_icon,
            width=32,
            fg_color="transparent",
            hover_color="#e0e0e0",
            command=lambda r=recipe:
                edit_recipe.show_edit_recipe_screen(parent_frame, r, lang)
        ).pack(side="right", padx=(0, 5))

        # Delete
        ctk.CTkButton(
            row,
            text=delete_icon,
            width=32,
            fg_color="transparent",
            hover_color="#f8d7da",
            text_color="#dc3545",
            command=lambda r=recipe:
                delete_recipe(r, parent_frame, list_frame, lang)
        ).pack(side="right", padx=(0, 10))


def delete_recipe(recipe_name, parent_frame, list_frame, language):
    database.delete_recipe(recipe_name)
    recipes = database.get_recipe_names()
    recipe_list(list_frame, recipes, parent_frame, language)


def apply_filter(list_frame, category, parent_frame, language):
    if category:
        recipes = database.categoryFilter(category)
    else:
        recipes = database.get_recipe_names()

    recipe_list(list_frame, recipes, parent_frame, language)


def show_manage_recipe_screen(parent_frame, language):
    lang = language

    # 🔴 EN ÖNEMLİ SATIR
    for widget in parent_frame.winfo_children():
        widget.destroy()

    container = ctk.CTkFrame(parent_frame)
    container.pack(fill="both", expand=True, padx=30, pady=30)

    # Header
    ctk.CTkLabel(
        container,
        text=texts[lang]["manage_recipes_title"],
        font=ctk.CTkFont(size=22, weight="bold")
    ).pack(anchor="w", pady=(0, 20))

    # Category filter
    categories = list(set(
        database.get_recipe_category() + [
            "", "Barbecue","Beef","Bread","Cake","Casserole","Chicken",
            "Chocolate","Cookie","Egg","Fish","Lamb","Muffin",
            "Noodle","Pasta","Pie","Pork","Rice","Salad",
            "Sandwich","Sauce","Soup","Tart","Vegetable","Vegetarian"
        ]
    ))

    ctk.CTkLabel(
        container,
        text=texts[lang]["category_label"]
    ).pack(anchor="w")

    selected_category = ctk.StringVar(value="")
    category_combo = ctk.CTkComboBox(
        container,
        values=categories,
        variable=selected_category,
        width=220
    )
    category_combo.pack(anchor="w", pady=(5, 20))

    # Scrollable list
    list_frame = ctk.CTkScrollableFrame(container)
    list_frame.pack(fill="both", expand=True)

    category_combo.configure(
        command=lambda value:
            apply_filter(list_frame, value, parent_frame, lang)
    )

    recipes = database.get_recipe_names()
    recipe_list(list_frame, recipes, parent_frame, lang)
