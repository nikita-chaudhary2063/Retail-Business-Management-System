class Reports:
    def __init__(self, inventory):
        self.inventory = inventory

    def low_stock_report(self):
        found = False

        print("\n===== LOW STOCK REPORT =====")

        for product in self.inventory.products.values():
            if product.quantity <= 5:
                print("Product:", product.name)
                print("Product ID:", product.product_ID)
                print("Remaining stock:", product.quantity)
                print("---------------------------")
                found = True

        if not found:
            print("No low-stock products found!")

    def inventory_value_report(self):
        total_value = 0

        print("\n===== INVENTORY VALUE REPORT =====")

        for product in self.inventory.products.values():
            product_value = product.price * product.quantity
            total_value += product_value

        print("Total Inventory Value: Rs.", total_value)