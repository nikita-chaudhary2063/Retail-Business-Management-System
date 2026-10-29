
from product import Product

import json

class Storage:
    def __init__(self):
        self.filename="products.json" #stores filename in an instance attribute.

    def save_products(self,products):
        products_data=[]

        for product in products.values():
            product_dict={
                "product_id":product.product_ID,
                "name":product.name,
                "price":product.price,
                "quantity":product.quantity
            }
            products_data.append(product_dict)

        with open(self.filename,"w") as file:
            json.dump(products_data,file,indent=5)

    def load_products(self):
        with open(self.filename,"r") as file:
            products_data=json.load(file)

            products={}

            for item in products_data:
                product=Product(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["quantity"]
                )

                products[product.product_ID]=product

                return products
