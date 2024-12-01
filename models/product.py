from models.entity import Entity

class Product(Entity):
    def __init__(self, product_id, name, price, stock):
        super().__init__(product_id)
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "Product ID": self.entity_id,
            "Name": self.name,
            "Price": self.price,
            "Stock": self.stock,
        }

    def update_stock(self, quantity):
        self.stock += quantity

    def __str__(self):
        return f"Product(ID: {self.entity_id}, Name: {self.name}, Stock: {self.stock})"
