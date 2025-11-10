import tkinter as tk
from tkinter import ttk 

import dashboard
import add_recipe 
import manage_recipes
import settings

current_lang = "en"  

root = tk.Tk()
root.title("Recipe Keeper")
root.geometry("1200x600")

# --- Sidebar Frame ---

sidebar_frame = tk.Frame(root, bg="#f0f0f0", width=200, relief=tk.RAISED, bd=1)
sidebar_frame.pack(side="left", fill="y")
sidebar_frame.pack_propagate(False) #constant width
app_title = tk.Label(sidebar_frame, text="Recipe Keeper", bg="#f0f0f0", font=("Arial", 14, "bold"), pady=10)
app_title.pack(pady=(10, 20))


def menu_click(button_text):
    for widget in main_content_frame.winfo_children():
        widget.destroy()
    current_lang = settings.get_lang()
    if (button_text == "Dashboard"):
        dashboard.show_dashboard(main_content_frame, current_lang)

    elif (button_text == "Add Recipe"):
        print("add recipe clicked.")
        add_recipe.show_add_recipe_screen(main_content_frame, current_lang)

    elif (button_text == "Manage Recipes"):
        print("manage recipe clicked.")
        manage_recipes.show_manage_recipe_screen(main_content_frame, current_lang)

    elif (button_text == "Settings"):
        settings.show_settings(main_content_frame, current_lang)
    
    
   

menu_items = ["Dashboard", "Add Recipe", "Manage Recipes","Settings"]

for text in menu_items:
    button = tk.Button(
        sidebar_frame, 
        text=f"{text}", 
        anchor="w", 
        padx=10,
        font=("Arial", 12),
        bg="#f0f0f0", 
        fg="black", 
        relief=tk.FLAT, 
        activebackground="#e0e0e0", 
        command=lambda t=text: menu_click(t) 
    )
    button.pack(fill="x", pady=2) 


# --- Main Content Frame---
main_content_frame = tk.Frame(root, bg="white")
main_content_frame.pack(side="right", fill="both", expand=True) 

tk.Label(main_content_frame, text="All your recipes in one place", font=("Arial", 24, "bold"), bg="white", pady=20).pack(pady=20)


root.mainloop()