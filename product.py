class Product:
    def __init__(self,product_id,name,price,quantity):
       self.product_ID=product_id
       self.name=name
       self._price=price
       self._quantity=quantity

    def display_info(self):
        print("Product ID:",self.product_ID)
        print("Product name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value<0:
            raise ValueError("Price cannot be negative")
        else:
            self._price=value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        if value<0:
            raise ValueError("Quantity cannot be negative")
        else:
            self._quantity=value

            
        
    
        