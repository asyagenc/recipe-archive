import sqlite3

DATABASE_NAME = 'recipe.db'

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
    try:
        cursor.execute("""
            INSERT INTO Recipes (name, category, collection, ingredients, instructions, cooking_time, portion, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, category, collection, ingredients, instructions, cooking_time, portion, notes))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False, "A recipe with that name already exists."
    except sqlite3.Error as e:
        print(f"Error adding recipe: {e}")
        return False, "A database error occurred."
    finally:
        conn.close()


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
    
    


def categoryFilter(categoryName):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Recipes WHERE category = ?", (categoryName,))
    recipes = cursor.fetchall()
    conn.close()
    return [r[0] for r in recipes]

def get_total_recipe_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Recipes")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_latest_recipes(limit=5):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name 
        FROM Recipes
        ORDER BY rowid DESC
        LIMIT ?
    """, (limit,))
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
    cursor.execute("""
        UPDATE Recipes
        SET name = ?, category = ?, collection = ?, ingredients = ?, instructions = ?, cooking_time = ?, portion = ?, notes = ?
        WHERE name = ?
    """, (name, category, collection, ingredients, instructions, cooking_time, portion, notes, old_name))
    conn.commit()
    conn.close()



if __name__ == '__main__':
    setup_database()
