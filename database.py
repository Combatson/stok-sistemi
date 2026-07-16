import sqlite3
def create_table():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        price REAL NOT NULL CHECK(price >= 0),
        stock_quantity INTEGER NOT NULL CHECK(stock_quantity >= 0)
    )
    """)

    connection.commit()
    connection.close()
def add_product_to_database(name, price, stock_quantity):
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    
    cursor.execute("""
                   INSERT INTO products (name, price, stock_quantity)
                   VALUES (?, ?, ?)
                   """, (name, price, stock_quantity))
    connection.commit()
    connection.close()
def get_all_products():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    connection.close()
    return products
def search_product_in_database(name):
        connection = sqlite3.connect("inventory.db")
        cursor = connection.cursor()
        cursor.execute(
        "SELECT * FROM products WHERE name = ?",
        (name,)
        )
        product = cursor.fetchone()
        connection.close()
        return product
def remove_product_from_database(name):
     connection = sqlite3.connect("inventory.db")
     cursor = connection.cursor()
     cursor.execute("""
                    DELETE FROM products WHERE name =?""",
                    (name,))
     deleted_count = cursor.rowcount
     connection.commit()
     connection.close()
     return deleted_count
def update_product_in_database(name, price, stock_quantity):
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    cursor.execute("""
                   UPDATE products
                     SET price = ?, stock_quantity = ?
                     WHERE name = ?
                   """, (price, stock_quantity, name))
    updated_count = cursor.rowcount
    connection.commit()
    connection.close()
    return updated_count
def get_low_stock_products_from_database(limit):
     connection = sqlite3.connect("inventory.db")
     cursor = connection.cursor()

     cursor.execute("""
                    SELECT * FROM products WHERE stock_quantity < ?
                    """, (limit,))
     low_stock_products = cursor.fetchall()
     connection.close()
     return low_stock_products

create_table()
