import customtkinter as ctk
from tkinter import messagebox

import database
from texts import texts


def show_add_recipe_screen(parent_frame, language):
    lang = language

    # EKRANI TEMİZLE
    for widget in parent_frame.winfo_children():
        widget.destroy()

    container = ctk.CTkFrame(parent_frame)
    container.pack(fill="both", expand=True, padx=30, pady=30)

    # TITLE
    ctk.CTkLabel(
        container,
        text=texts[lang]["new_recipe_title"],
        font=ctk.CTkFont(size=22, weight="bold")
    ).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 20))

    # ---------- LEFT CARD ----------
    left = ctk.CTkFrame(container)
    left.grid(row=1, column=0, sticky="nsew", padx=10)

    ctk.CTkLabel(left, text=texts[lang]["name_label"]).pack(anchor="w", padx=15, pady=(15, 5))
    name_entry = ctk.CTkEntry(left, width=220)
    name_entry.pack(padx=15, pady=(0, 10))

    categories = list(set(database.get_recipe_category() + [
        "Barbecue","Beef","Bread","Cake","Casserole","Chicken",
        "Chocolate","Cookie","Egg","Fish","Lamb","Muffin",
        "Noodle","Pasta","Pie","Pork","Rice","Salad",
        "Sandwich","Sauce","Soup","Tart","Vegetable","Vegetarian"
    ]))

    ctk.CTkLabel(left, text=texts[lang]["category_label"]).pack(anchor="w", padx=15, pady=(10, 5))
    category_combo = ctk.CTkComboBox(left, values=categories)
    category_combo.pack(padx=15, pady=(0, 10))

    collections = list(set(database.get_recipe_collection() + ["My Recipes"]))
    ctk.CTkLabel(left, text=texts[lang]["collection_label"]).pack(anchor="w", padx=15, pady=(10, 5))
    collection_combo = ctk.CTkComboBox(left, values=collections)
    collection_combo.pack(padx=15, pady=(0, 10))

    ctk.CTkLabel(left, text=texts[lang]["portion_label"]).pack(anchor="w", padx=15, pady=(10, 5))
    portion_var = ctk.IntVar(value=1)
    portion_entry = ctk.CTkEntry(left, textvariable=portion_var, width=60)
    portion_entry.pack(padx=15, pady=(0, 15))

    # Cooking time
    ctk.CTkLabel(left, text=texts[lang]["cooking_time_label"]).pack(anchor="w", padx=15, pady=(10, 5))
    time_row = ctk.CTkFrame(left, fg_color="transparent")
    time_row.pack(anchor="w", padx=15, pady=(0, 15))

    hours_var = ctk.IntVar(value=0)
    minutes_var = ctk.IntVar(value=30)

    ctk.CTkEntry(time_row, textvariable=hours_var, width=50).pack(side="left")
    ctk.CTkLabel(time_row, text=":").pack(side="left", padx=5)
    ctk.CTkEntry(time_row, textvariable=minutes_var, width=50).pack(side="left")

    # ---------- INGREDIENTS ----------
    ingredients = ctk.CTkFrame(container)
    ingredients.grid(row=1, column=1, sticky="nsew", padx=10)

    ctk.CTkLabel(
        ingredients,
        text=texts[lang]["ingredients_label"],
        font=ctk.CTkFont(weight="bold")
    ).pack(anchor="w", padx=15, pady=(15, 5))

    ingredients_text = ctk.CTkTextbox(ingredients)
    ingredients_text.pack(fill="both", expand=True, padx=15, pady=10)

    # ---------- DIRECTIONS ----------
    directions = ctk.CTkFrame(container)
    directions.grid(row=1, column=2, sticky="nsew", padx=10)

    ctk.CTkLabel(
        directions,
        text=texts[lang]["directions_label"],
        font=ctk.CTkFont(weight="bold")
    ).pack(anchor="w", padx=15, pady=(15, 5))

    directions_text = ctk.CTkTextbox(directions)
    directions_text.pack(fill="both", expand=True, padx=15, pady=10)

    # ---------- SAVE ----------
    def save_recipe():
        cooking_time = hours_var.get() * 60 + minutes_var.get()

        database.add_recipe(
            name_entry.get(),
            category_combo.get(),
            collection_combo.get(),
            ingredients_text.get("1.0", "end").strip(),
            directions_text.get("1.0", "end").strip(),
            cooking_time,
            portion_var.get(),
            notes=""
        )

        messagebox.showinfo(
            texts[lang]["saved_message_title"],
            texts[lang]["saved_message_text"]
        )

    ctk.CTkButton(
        container,
        text=texts[lang]["save_button"],
        height=44,
        command=save_recipe
    ).grid(row=2, column=2, sticky="e", pady=20)

    container.grid_columnconfigure((0, 1, 2), weight=1)
    container.grid_rowconfigure(1, weight=1)
