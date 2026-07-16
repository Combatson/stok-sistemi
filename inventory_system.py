from database import (
    add_product_to_database,
    get_all_products,
    search_product_in_database,
    remove_product_from_database,
    update_product_in_database,
    get_low_stock_products_from_database
)
from config import ADMIN_EMAIL, ADMIN_PASSWORD

def view_low_stock_products():
    try:
        limit = int(input("Enter the stock quantity limit: "))
        if limit < 0:
            print("Limit must be a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    low_stock_products = get_low_stock_products_from_database(limit)

    if low_stock_products:
        print(f"Products with stock quantity less than {limit}:")
        for product in low_stock_products:
            print(
                f"ID: {product[0]}, "
                f"Name: {product[1]}, "
                f"Price: {product[2]}, "
                f"Stock Quantity: {product[3]}"
            )
    else:
        print(f"No products found with stock quantity less than {limit}.")
def add_product():
    product_name = input("Enter product name: ").strip()
    if product_name:
        existing_product = search_product_in_database(product_name)
        if existing_product:
            print("Product already exists.")
            return
        try:
            product_price = float(input("Enter product price: "))
            product_stock_quantity = int(input("Enter product stock quantity: "))
            if product_price < 0 or product_stock_quantity < 0:
                print("Price and stock quantity must be non-negative.")
                return
            add_product_to_database(product_name, product_price, product_stock_quantity)
            print("Product successfully added.")
        except ValueError:
            print("Invalid input. Please enter numeric values for price and stock quantity.")
    else:
        print("Invalid product name.")
def remove_product():
    product_name = input("Enter product name to remove: ").strip()
    if product_name:
        deleted_count = remove_product_from_database(product_name)
        if deleted_count > 0:
            print("Product successfully removed.")
        else:
            print("Product not found.")
    else:
        print("Invalid product name.")
def update_product():
    product_name = input("Enter product name to update: ").strip()
    if product_name:
        product = search_product_in_database(product_name)
        if product:
            try:
                new_price = float(input("Enter new product price: "))
                new_stock_quantity = int(input("Enter new product stock quantity: "))
                if new_price < 0 or new_stock_quantity < 0:
                    print("Price and stock quantity must be non-negative.")
                    return
                updated_count = update_product_in_database(product_name, new_price, new_stock_quantity)
                if updated_count > 0:
                    print("Product successfully updated.")
                else:
                    print("Failed to update product.")
            except ValueError:
                print("Invalid input. Please enter numeric values for price and stock quantity.")
        else:
            print("Product not found.")
    else:
        print("Invalid product name.")
def view_products():
    products = get_all_products()

    if products:
        print("Products:")

        for product in products:
            print(
                f"ID: {product[0]}, "
                f"Name: {product[1]}, "
                f"Price: {product[2]}, "
                f"Stock Quantity: {product[3]}"
            )
    else:
        print("No products found.")
def admin_login():
    email = input("Enter admin email: ")
    password = input("Enter admin password: ")
    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        print("Admin login successful.")
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Update Product")
            print("4. View Products")
            print("5. Search Product")
            print("6. Logout")
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                add_product()
            elif choice == "2":
                remove_product()
            elif choice == "3":
                update_product()
            elif choice == "4":
                view_products()
            elif choice == "5":
                search_product()
            elif choice == "6":
                view_low_stock_products()
            elif choice == "7":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid admin credentials.")
def search_product():
    product_name = input("Enter product name to search: ").strip()
    if product_name:
        product = search_product_in_database(product_name)
        if product:
            print(
                f"ID: {product[0]}, "
                f"Name: {product[1]}, "
                f"Price: {product[2]}, "
                f"Stock Quantity: {product[3]}"
            )
        else:
            print("Product not found.")
    else:
        print("Invalid product name.")

admin_login()
