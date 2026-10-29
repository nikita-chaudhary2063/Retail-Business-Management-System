from product import Product

class Inventory:
    def __init__(self):
        self.products={

        }

    def add_products(self,product):
        if product.product_ID in self.products:
            print("Product already exists!")

        else:
            self.products[ product.product_ID]=product
            print("Product added successfully!")

    def view_products(self):
        if not self.products:
            print("No product available!")

        else:
            for  product in self.products.values():
                product.display_info()

    def search_product(self,product_id):
        if product_id in self.products:
            self.products[product_id].display_info()
        else:
            print("Product not found!")

    def remove_product(self,product_id):
        if product_id in self.products:
            self.products.pop(product_id)
            print("Product removed successfully!")

        else:
            print("Product not found!")

