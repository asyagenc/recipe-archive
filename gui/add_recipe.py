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
    title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="w")

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
    portion_spin.grid(row=7, column=0, sticky="w", padx=10, pady=5)



    # ------------------------------------------------
    # Cooking Time
    # ------------------------------------------------

    cooking_time_label = tk.Label(recipe_frame, text=texts[current_lang]["cooking_time_label"], bg=recipe_frame.cget("bg"))
    cooking_time_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)

    time_input_frame = tk.Frame(recipe_frame, bg=recipe_frame.cget("bg"))
    time_input_frame.grid(row=9, column=0, sticky="w", padx=10, pady=5)

    cooking_hours_var = tk.IntVar(value=0) 
    cooking_hours_spin = tk.Spinbox(
        time_input_frame, 
        from_=0, 
        to=24, 
        increment=1, 
        textvariable=cooking_hours_var, 
        width=3, 
        wrap=True 
    )
    cooking_hours_spin.pack(side=tk.LEFT, padx=(0, 2))

    separator_label = tk.Label(time_input_frame, text=":", bg=recipe_frame.cget("bg"), font=("Arial", 10, "bold"))
    separator_label.pack(side=tk.LEFT)

    cooking_minutes_var = tk.IntVar(value=30) 
    cooking_minutes_spin = tk.Spinbox(
        time_input_frame, 
        from_=0, 
        to=59, 
        increment=5, 
        textvariable=cooking_minutes_var, 
        width=3, 
        wrap=True
    )
    cooking_minutes_spin.pack(side=tk.LEFT, padx=(2, 0))
    #-------
    
    ingredients_frame = tk.Frame(parent_frame, bg=parent_frame.cget("bg"), relief=tk.RAISED, bd=1) 
    ingredients_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    ingredients_label = tk.Label(ingredients_frame, text=texts[current_lang]["ingredients_label"], bg=ingredients_frame.cget("bg")) 
    ingredients_label.grid(row=0, column=0, sticky="w", padx=10, pady=5) 
    ingredients_text = tk.Text(ingredients_frame, width=40, height=20) 
    ingredients_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    direction_frame = tk.Frame(parent_frame, bg=parent_frame.cget("bg"), relief=tk.RAISED, bd=1)
    direction_frame.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

    directions_label = tk.Label(direction_frame, text=texts[current_lang]["directions_label"], bg=direction_frame.cget("bg"))
    directions_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    directions_text = tk.Text(direction_frame, width=40, height=20)
    directions_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


    def save_recipe():
        name = name_entry.get()
        name_entry.delete(0, "end")
        category = selectedCategory.get()
        collection = selectedCollection.get()
        portion = portion_var.get()
        #--
        hours = cooking_hours_var.get()
        minutes = cooking_minutes_var.get()
        cooking_time = (hours * 60) + minutes
        #---
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
    save_button.grid(row=2, column=2, columnspan=5, sticky="e", padx=(0, 10), pady=10)
