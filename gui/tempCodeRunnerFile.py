import customtkinter as ctk
from tkinter import messagebox

import database
from texts import texts
import manage_recipes


def show_edit_recipe_screen(parent_frame, recipe_name, language="en"):
    lang = language

    # Clear screen
    for widget in parent_frame.winfo_children():
        widget.destroy()

    recipe = database.get_recipe_by_name(recipe_name)
    if not recipe:
        messagebox.showerror("Error", "Recipe not found")
        return

    (
        old_name,
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
        text=texts[lang]["edit_recipe_title"],
        font=ctk.CTkFont(size=22, weight="bold")
    ).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 20))

    # -------------------------
    # LEFT – BASIC INFO
    # -------------------------
    left = ctk.CTkFrame(container)
    left.grid(row=1, column=0, sticky="nsew", padx=10)

    ctk.CTkLabel(left, text=texts[lang]["name_label"]).pack(anchor="w", padx=15, pady=(15, 5))
    name_entry = ctk.CTkEntry(left, width=220)
    name_entry.insert(0, old_name)
    name_entry.pack(padx=15, pady=(0, 10))

    categories = list(set(database.get_recipe_category()))
    ctk.CTkLabel(left, text=texts[lang]["category_label"]).pack(anchor="w", padx=15, pady=(10, 5))
    category_combo = ctk.CTkComboBox(left, values=categories)
    category_combo.set(category)
    category_combo.pack(padx=15, pady=(0, 10))

    collections = list(set(database.get_recipe_collection()))
    ctk.CTkLabel(left, text=texts[lang]["collection_label"]).pack(anchor="w", padx=15, pady=(10, 5))
    collection_combo = ctk.CTkComboBox(left, values=collections)
    collection_combo.set(collection)
    collection_combo.pack(padx=15, pady=(0, 10))

    ctk.CTkLabel(left, text=texts[lang]["portion_label"]).pack(anchor="w", padx=15, pady=(10, 5))
    portion_var = ctk.IntVar(value=portion)
    portion_entry = ctk.CTkEntry(left, textvariable=portion_var, width=60)
    portion_entry.pack(padx=15, pady=(0, 15))

    # Cooking time
    ctk.CTkLabel(left, text=texts[lang]["cooking_time_label"]).pack(anchor="w", padx=15, pady=(10, 5))

    hours_var = ctk.IntVar(value=cooking_time // 60)
    minutes_var = ctk.IntVar(value=cooking_time % 60)

    time_row = ctk.CTkFrame(left, fg_color="transparent")
    time_row.pack(anchor="w", padx=15, pady=(0, 15))

    ctk.CTkEntry(time_row, textvariable=hours_var, width=50).pack(side="left")
    ctk.CTkLabel(time_row, text=":").pack(side="left", padx=5)
    ctk.CTkEntry(time_row, textvariable=minutes_var, width=50).pack(side="left")

    # -------------------------
    # MIDDLE – INGREDIENTS
    # -------------------------
    mid = ctk.CTkFrame(container)
    mid.grid(row=1, column=1, sticky="nsew", padx=10)

    ctk.CTkLabel(mid, text=texts[lang]["ingredients_label"], font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=15, pady=(15, 5))
    ingredients_box = ctk.CTkTextbox(mid, width=350, height=300)
    ingredients_box.insert("1.0", ingredients)
    ingredients_box.pack(padx=15, pady=10, fill="both", expand=True)

    # -------------------------
    # RIGHT – DIRECTIONS
    # -------------------------
    right = ctk.CTkFrame(container)
    right.grid(row=1, column=2, sticky="nsew", padx=10)

    ctk.CTkLabel(right, text=texts[lang]["directions_label"], font=ctk.CTkFont(weight="bold")).pack(anchor="w", padx=15, pady=(15, 5))
    directions_box = ctk.CTkTextbox(right, width=350, height=300)
    directions_box.insert("1.0", instructions)
    directions_box.pack(padx=15, pady=10, fill="both", expand=True)

    # -------------------------
    # SAVE
    # -------------------------
    def save_changes():
        cooking_time_new = (hours_var.get() * 60) + minutes_var.get()

        database.update_recipe(
            old_name,
            name_entry.get(),
            category_combo.get(),
            collection_combo.get(),
            ingredients_box.get("1.0", "end").strip(),
            directions_box.get("1.0", "end").strip(),
            cooking_time_new,
            portion_var.get(),
            notes=""
        )

        messagebox.showinfo(
            texts[lang]["saved_message_title"],
            texts[lang]["saved_message_text"]
        )

        manage_recipes.show_manage_recipe_screen(parent_frame, lang)

    save_btn = ctk.CTkButton(
        container,
        text=texts[lang]["save_button"],
        height=44,
        corner_radius=12,
        command=save_changes
    )
    save_btn.grid(row=2, column=2, sticky="e", pady=20)

    # Layout weights
    container.grid_columnconfigure((0, 1, 2), weight=1)
    container.grid_rowconfigure(1, weight=1)
