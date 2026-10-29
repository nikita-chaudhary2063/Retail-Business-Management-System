from product import Product
from inventory import Inventory
from storage import Storage
from sales import Sales
from reports import Reports


# Create objects
storage1 = Storage()
inventory1 = Inventory()

inventory1.products = storage1.load_products()

sales1 = Sales(inventory1, storage1)
reports1 = Reports(inventory1)


while True:
    print("\n===== RETAIL BUSINESS MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Remove Product")
    print("5. Sell Product")
    print("6. Generate Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")

        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))

            if price < 0 or quantity < 0:
                print("Price and quantity cannot be negative!")
                continue

            if product_id in inventory1.products:
                print("Product ID already exists!")
                continue

            product = Product(product_id, name, price, quantity)

            inventory1.add_products(product)
            storage1.save_products(inventory1.products)

            print("Product added successfully!")

        except ValueError:
            print("Please enter a valid price and quantity!")

    elif choice == "2":
        inventory1.view_products()

    elif choice == "3":
        product_id = input("Enter product ID to search: ")
        inventory1.search_product(product_id)

    elif choice == "4":
        product_id = input("Enter product ID to remove: ")

        inventory1.remove_product(product_id)
        storage1.save_products(inventory1.products)

    elif choice == "5":
        product_id = input("Enter product ID to sell: ")

        try:
            quantity = int(input("Enter quantity to sell: "))
            sales1.sell_product(product_id, quantity)

        except ValueError:
            print("Please enter a valid quantity!")

    elif choice == "6":
        while True:
            print("\n===== REPORTS MENU =====")
            print("1. Low Stock Report")
            print("2. Total Inventory Value")
            print("3. Back to Main Menu")

            report_choice = input("Enter your choice: ")

            if report_choice == "1":
                reports1.low_stock_report()

            elif report_choice == "2":
                reports1.inventory_value_report()

            elif report_choice == "3":
                break

            else:
                print("Invalid choice! Please try again.")

    elif choice == "7":
        print("Thank you for using the Retail Business Management System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 7.")