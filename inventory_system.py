from config import ADMIN_EMAIL, ADMIN_PASSWORD
import json
try:
    with open("product.json", "r") as document:
        data = json.load(document)
except FileNotFoundError:
    data = {}
    print("No product.json file found. Creating a new one.")
def view_low_stock_products():
    for product_name, product_details in data.items():
        if product_details['stock_quantity'] < 5:
            print("Low Stock Products:")
            print(f"Name: {product_name}, Price: {product_details['price']}, Stock Quantity: {product_details['stock_quantity']}")
            print("This product is low in stock. Please consider restocking.")
def save_data():
    with open("product.json", "w") as document:
        json.dump(data, document) 
def add_product():
    product_name = input("Enter product name: ")
    if product_name in data:
        print("Product already exists.")
        return
    else:
        data[product_name] = {}
        save_data()
        print("Product successfully added. Please add product details.")    
        try:
            product_price = float(input("Enter product price: "))
            data[product_name]["price"] = product_price
            print("Product details successfully added.")
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            del data[product_name]  # Remove the product if price input is invalid
            save_data()
            return
        try:
            product_stock_quantity = int(input("Enter product stock quantity: "))
            data[product_name]["stock_quantity"] = product_stock_quantity
            print("Product details successfully added.")
        except ValueError:
            print("Invalid stock quantity. Please enter a numeric value.")
            del data[product_name]  # Remove the product if stock quantity input is invalid
            save_data()
            return
        save_data()
def remove_product():
    product_name = input("Enter product name to remove: ")
    if product_name in data:
        del data[product_name]
        save_data()
        print("Product successfully removed.")
    else:
        print("Product not found.")
def update_product():
    product_name = input("Enter product name to update: ")
    if product_name in data:
        try:
            product_price = float(input("Enter new product price: "))
            data[product_name]["price"] = product_price
            print("Product price successfully updated.")
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            return
        try:
            product_stock_quantity = int(input("Enter new product stock quantity: "))
            data[product_name]["stock_quantity"] = product_stock_quantity
            print("Product stock quantity successfully updated.")
        except ValueError:
            print("Invalid stock quantity. Please enter a numeric value.")
            return
        save_data()
    else:
        print("Product not found.")
def view_products():
    if data:
        print("Products:")
        for product_name, product_details in data.items():
            print(f"Name: {product_name}, Price: {product_details['price']}, Stock Quantity: {product_details['stock_quantity']}")
        view_low_stock_products()
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
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid admin credentials.")
def search_product():   
    product_name = input("Enter product name to search: ").strip()
    if product_name in data:
        product_details = data[product_name]
        print(f"Name: {product_name}, Price: {product_details['price']}, Stock Quantity: {product_details['stock_quantity']}")
    else:
        print("Product not found.")

admin_login()
