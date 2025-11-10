import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import database 
import manage_recipes
from texts import texts  

def show_add_recipe_screen(parent_frame, language):
    current_lang = language  

    title_label = tk.Label(
        parent_frame, 
        text=texts[current_lang]["new_recipe_title"], 
        bg=parent_frame.cget("bg"), 
        font=("Helvetica", 16, "bold")
    )
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    recipe_frame = tk.Frame(parent_frame, bg=parent_frame.cget("bg"), relief=tk.RAISED, bd=1)
    recipe_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    name_label = tk.Label(recipe_frame, text=texts[current_lang]["name_label"], bg=recipe_frame.cget("bg"))
    name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    name_entry = ttk.Entry(recipe_frame, width=30)
    name_entry.grid(row=1, column=0, padx=10, pady=5)
    
    categories = database.get_recipe_category()
    categories.extend([
        "Barbecue","Beef","Bread","Cake","Casserole","Chicken",
        "Chocolate","Cookie","Egg","Fish","Lamb","Muffin",
        "Noodle","Pasta","Pie","Pork","Rice","Salad",
        "Sandwich","Sauce","Soup","Tart","Vegetable","Vegetarian"
    ])
    categories = list(set(categories))

    category_label = tk.Label(recipe_frame, text=texts[current_lang]["category_label"], bg=recipe_frame.cget("bg"))
    category_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    selectedCategory = tk.StringVar()
    categoryCombo = ttk.Combobox(recipe_frame, textvariable=selectedCategory, values=categories)
    categoryCombo.current(0)
    categoryCombo.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    collection = database.get_recipe_collection()
    collection.extend([
        "My Recipies"
    ])
    collection = list(set(collection))

    collection_label = tk.Label(recipe_frame, text=texts[current_lang]["collection_label"], bg=recipe_frame.cget("bg"))
    collection_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    selectedCollection = tk.StringVar()
    collectionCombo = ttk.Combobox(recipe_frame, textvariable=selectedCollection, values=collection)
    collectionCombo.current(0)
    collectionCombo.grid(row=5, column=0, sticky="w", padx=10, pady=5)

    portion_label = tk.Label(recipe_frame, text=texts[current_lang]["portion_label"], bg=recipe_frame.cget("bg"))
    portion_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)

    portion_var = tk.IntVar(value=1)
    portion_spin = tk.Spinbox(recipe_frame, from_=0, to=100, increment=1, textvariable=portion_var, width=5)
    portion_spin.grid(row=7, column=0, padx=10, pady=5)

    cooking_time_label = tk.Label(recipe_frame, text=texts[current_lang]["cooking_time_label"], bg=recipe_frame.cget("bg"))
    cooking_time_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)

    cooking_var = tk.IntVar(value=1)
    cooking_spin = tk.Spinbox(recipe_frame, from_=0, to=100, increment=1, textvariable=cooking_var, width=5)
    cooking_spin.grid(row=9, column=0, padx=10, pady=5)
    
    ingredients_frame = tk.Frame(parent_frame, bg=parent_frame.cget("bg"), relief=tk.RAISED, bd=1) 
    ingredients_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    ingredients_label = tk.Label(ingredients_frame, text=texts[current_lang]["ingredients_label"], bg=ingredients_frame.cget("bg")) 
    ingredients_label.grid(row=0, column=0, sticky="w", padx=10, pady=5) 
    ingredients_text = tk.Text(ingredients_frame, width=40, height=20) 
    ingredients_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

    direction_frame = tk.Frame(parent_frame, bg=parent_frame.cget("bg"), relief=tk.RAISED, bd=1)
    direction_frame.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

    directions_label = tk.Label(direction_frame, text=texts[current_lang]["directions_label"], bg=direction_frame.cget("bg"))
    directions_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    directions_text = tk.Text(direction_frame, width=40, height=20)
    directions_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

    def save_recipe():
        name = name_entry.get()
        name_entry.delete(0, "end")
        category = selectedCategory.get()
        collection = selectedCollection.get()
        portion = portion_var.get()
        cooking_time = cooking_var.get()
        ingredients = ingredients_text.get("1.0", "end-1c")
        ingredients_text.delete("1.0", "end")  
        directions = directions_text.get("1.0", "end-1c")
        directions_text.delete("1.0", "end")    

        database.add_recipe(
            name,
            category,
            collection,
            ingredients,
            directions,
            cooking_time,
            portion,
            notes=""
        )
        messagebox.showinfo(
            texts[current_lang]["saved_message_title"],
            texts[current_lang]["saved_message_text"]
        )
        print("Recipe Saved")
        print("--------------------------")

    parent_frame.grid_columnconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_columnconfigure(2, weight=1)
    parent_frame.grid_rowconfigure(1, weight=1)

    save_button = ttk.Button(parent_frame, text=texts[current_lang]["save_button"], command=save_recipe)
    save_button.grid(row=2, column=0, columnspan=3, pady=10)
