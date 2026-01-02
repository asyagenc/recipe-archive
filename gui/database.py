import sqlite3
from texts import texts
DATABASE_NAME = 'recipe.db'

CATEGORY_TR_TO_EN = dict(
    zip(
        texts["tr"]["category_items"],
        texts["en"]["category_items"]
    )
)

CATEGORY_EN_TO_TR = dict(
    zip(
        texts["en"]["category_items"],
        texts["tr"]["category_items"]
    )
)

def category_for_db(category):
    return CATEGORY_TR_TO_EN.get(category, category)

def category_for_ui(category_en, lang):
    if lang == "tr":
        return CATEGORY_EN_TO_TR.get(category_en, category_en)
    return category_en


    #------------
def setup_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Recipes (
                name TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL,
                collection TEXT,
                ingredients TEXT NOT NULL,
                instructions TEXT NOT NULL,
                cooking_time INTEGER,
                portion INTEGER,
                notes TEXT 
            )
        """)
        conn.commit()
        print(f"Database '{DATABASE_NAME}' created.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)


def add_recipe(name, category, collection, ingredients, instructions, cooking_time, portion, notes=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    category_en = category_for_db(category)
    try:
        cursor.execute("""
            INSERT INTO Recipes (name, category, collection, ingredients, instructions, cooking_time, portion, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, category_en, collection, ingredients, instructions, cooking_time, portion, notes))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False, "A recipe with that name already exists."
    except sqlite3.Error as e:
        print(f"Error adding recipe: {e}")
        return False, "A database error occurred."
    finally:
        conn.close()
        
def get_category_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(DISTINCT category)
        FROM Recipes
        WHERE category IS NOT NULL AND category != ''
    """)
    count = cursor.fetchone()[0]
    conn.close()
    return count



def get_recipe_names():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Recipes")
    recipes = cursor.fetchall()
    conn.close()
    return [r[0] for r in recipes]


def get_recipe_category():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category FROM Recipes")
    recipes = cursor.fetchall()
    conn.close()
    return [r[0] for r in recipes]

def get_current_recipe_category(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category FROM Recipes WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def get_recipe_collection():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT collection FROM Recipes")
    recipes = cursor.fetchall()
    conn.close()
    return [r[0] for r in recipes]


def get_all_recipes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, category, collection, cooking_time, portion FROM Recipes")
    recipes = cursor.fetchall()
    conn.close()
    return recipes


def delete_recipe(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Recipes WHERE name = ?", (name,))
    conn.commit()
    conn.close()
    
    


def categoryFilter(category):
    conn = get_db_connection()
    cursor = conn.cursor()
    category_en = category_for_db(category)
    cursor.execute("SELECT name FROM Recipes WHERE category = ?", (category_en,))
    data = cursor.fetchall()
    conn.close()
    return [r[0] for r in data]

def get_total_recipe_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Recipes")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_latest_recipes():
    """Tüm tarifleri en yeniden en eskiye doğru sıralar"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name 
        FROM Recipes
        ORDER BY rowid DESC
    """)
    recipes = cursor.fetchall()
    conn.close()
    return [r[0] for r in recipes]
  

def get_recipe_by_name(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, category, collection, ingredients, instructions, cooking_time, portion, notes
        FROM Recipes
        WHERE name = ?
    """, (name,))
    recipe = cursor.fetchone()
    conn.close()
    return recipe

def update_recipe(old_name, name, category, collection, ingredients, instructions, cooking_time, portion, notes=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    category_en = category_for_db(category)
    cursor.execute("""
        UPDATE Recipes
        SET name = ?, category = ?, collection = ?, ingredients = ?, instructions = ?, cooking_time = ?, portion = ?, notes = ?
        WHERE name = ?
    """, (name, category_en, collection, ingredients, instructions, cooking_time, portion, notes, old_name))
    conn.commit()
    conn.close()



if __name__ == '__main__':
    setup_database()
