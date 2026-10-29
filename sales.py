class Sales:
    def __init__(self,inventory,storage):
        self.inventory=inventory
        self.storage=storage

    def sell_product(self,product_id,quantity):
        product=self.inventory.products.get(product_id)

        if product is None:
            print("Product not found!")
            return 
        
        if quantity<=0:
            print("Quantity must be greater than zero!")
            return

        if quantity>product.quantity:
            print("Insufficient stock!")
            print("Available quantity:",product.quantity)
            return

        total=product.price*self.quantity
        product.quantity-=quantity
        self.storage.save_products(self.inventory.products)

        print("Sale successful!")
        print("Product:", product.name)
        print("Quantity sold:", quantity)
        print("Total bill: Rs.", total)
        print("Remaining stock:", product.quantity)




