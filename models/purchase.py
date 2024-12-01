from models.entity import Entity

class Purchase(Entity):
    def __init__(self, purchase_id, customer_id, product_id, quantity, total_cost, date):
        super().__init__(purchase_id)
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_cost = total_cost
        self.date = date

    def to_dict(self):
        return {
            "Purchase ID": self.entity_id,
            "Customer ID": self.customer_id,
            "Product ID": self.product_id,
            "Quantity": self.quantity,
            "Total Cost": self.total_cost,
            "Date": self.date,
        }

    def __str__(self):
        return f"Purchase(ID: {self.entity_id}, Customer: {self.customer_id}, Total Cost: {self.total_cost})"
