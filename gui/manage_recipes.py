import tkinter as tk
from tkinter import ttk

import edit_recipe
import recipe_detail
import database
from texts import texts  

def recipe_list(frame, recipes, language):
    current_lang = language

    for widget in frame.winfo_children():
        widget.destroy()

    list_bg_color = "#FFFFFF" 
    edit_icon = texts[current_lang]["edit_icon"]
    delete_icon = texts[current_lang]["delete_icon"]

    for i, recipe in enumerate(recipes):
        row_frame = tk.Frame(frame, bg=list_bg_color, relief="flat")
        row_frame.pack(fill="x", ipady=5)

        recipe_label = tk.Label(
            row_frame, text=recipe, anchor="w", 
            bd=0, relief="flat", bg=list_bg_color, fg="#000000",
            font=('Helvetica', 14)
        )
        recipe_label.bind("<Button-1>", lambda event, r=recipe: menu_click(r, frame))
        recipe_label.pack(side="left", padx=10, fill="x", expand=True)

        edit_btn = tk.Button(
            row_frame, text=edit_icon, width=3,
            bd=0, relief="flat", bg=list_bg_color, fg="#007AFF", 
            font=('Helvetica', 10),
            command=lambda r=recipe: edit_bttn(r, frame)
        )
        edit_btn.pack(side="right", padx=(5, 1)) 
        
        delete_btn = tk.Button(
            row_frame, text=delete_icon, width=3,
            bd=0, relief="flat", bg=list_bg_color, fg="#FF3B30", 
            font=('Helvetica', 10),
            command=lambda r=recipe: delete_bttn(r, frame)
        )
        delete_btn.pack(side="right", padx=(1, 10)) 
        
        if i < len(recipes) - 1:
            separator = tk.Frame(frame, height=1, bg="#D1D1D6")
            separator.pack(fill="x", padx=10)


def show_manage_recipe_screen(parent_frame, language):
    current_lang = language

    categories = database.get_recipe_category()
    categories.extend([
        "Barbecue","Beef","Bread","Cake","Casserole","Chicken",
        "Chocolate","Cookie","Egg","Fish","Lamb","Muffin",
        "Noodle","Pasta","Pie","Pork","Rice","Salad",
        "Sandwich","Sauce","Soup","Tart","Vegetable","Vegetarian"
    ])
    categories = list(set(categories))

    category_label = tk.Label(parent_frame, text=texts[current_lang]["category_label"], bg=parent_frame.cget("bg"))
    category_label.pack(padx=10, pady=(10,0), anchor="w")

    selected = tk.StringVar()
    combo = ttk.Combobox(parent_frame, textvariable=selected, values=categories)
    combo.current(0)
    combo.pack(padx=10, pady=5, anchor="w")

    list_frame = tk.Frame(parent_frame)
    list_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    combo.bind("<<ComboboxSelected>>", lambda event: apply_filter(list_frame, selected.get(), current_lang))

    recipes = database.get_recipe_names()
    recipe_list(list_frame, recipes, current_lang)


def menu_click(item_name, frame):
    recipe_detail.show_recipe_screen(frame, item_name)

def edit_bttn(item_name, frame):
    edit_recipe.show_edit_recipe_screen(frame, item_name)

def delete_bttn(item_name, frame, language="en"):
    database.delete_recipe(item_name)
    recipes = database.get_recipe_names()
    recipe_list(frame, recipes, language)

def apply_filter(frame, category, language="en"):
    if category != "":
        recipes = database.categoryFilter(category)
        recipe_list(frame, recipes, language)
