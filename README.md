# CookBook - Modern Recipe Manager

CookBook is a sleek and modern desktop application built with the **CustomTkinter** library, allowing you to store, manage, and categorize your recipes digitally.

## Project Structure

The project is built with a modular structure:

- **main.py**: The main entry point of the application, managing theme and language settings.

- **gui/**: Contains the user interface modules:
  - **dashboard.py**: Main panel displaying statistics and recent recipes.
  - **add_recipe.py**: Screen for adding new recipes.
  - **manage_recipes.py**: Lists recipes with filtering and deletion functionality.
  - **edit_recipe.py**: Form for updating existing recipes.
  - **recipe_detail.py**: Screen to view recipe details.
  - **settings.py**: Settings page to manage language preferences.

- **database.py**: Handles SQLite database CRUD operations and category mappings.

- **texts.py**: Localized text for multilingual support (Turkish/English).

- **app_settings.json**: Configuration file storing the user's language preference.

- **recipe.db**: Local SQLite database storing all recipe data.

## Key Features

- Dynamic Dashboard: Track total recipes and category counts in real-time.  
- Smart Filtering: Quickly find recipes by their categories.  
- Multilingual Interface: Switch dynamically between Turkish and English.  
- Theme Support: Toggle between Dark and Light modes with a single click.  
- Modern GUI: Optimized user-friendly experience with CustomTkinter.

## Screens

**Dashboard**  
![Dashboard](recipe-archive/assets/image/dashboard.png)

**Adding a New Recipe**  
![Add Recipe](recipe-archive/assets/image/add%20recipe.png)

**Editing a Recipe**  
![Edit Recipe](recipe-archive/assets/image/edit%20recipe.png)

**Manage Recipes**  
![Manage Recipes](recipe-archive/assets/image/manage%20recipe.png)

**Dual Language Settings**  
![Dual Language Settings](recipe-archive/assets/image/dual%20lang%20settings.png)

**Dark Mode**  
![Dark Mode](recipe-archive/assets/image/dark%20mode.png)



## Installation & Running

1. **Install Dependencies**: The app requires `customtkinter` to run:

```bash
pip install customtkinter
```
2. **Run the Application**:
```bash
python main.py
```

## Technical Details

| Feature        | Details                  |
|----------------|--------------------------|
| UI Framework   | CustomTkinter            |
| Database       | SQLite3                  |
| Configuration  | JSON                     |
| Language       | Python 3.x               |
| Developer      | Asya Genç & Elif Oskanbaş|
| Version        | 1.0.0                    |




