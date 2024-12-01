from models.entity import Entity

class Customer(Entity):
    def __init__(self, customer_id, name, email, phone, is_active=True):
        super().__init__(customer_id)
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = is_active

    def to_dict(self):
        return {
            "Customer ID": self.entity_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Active": self.is_active,
        }

    def __str__(self):
        return f"Customer(ID: {self.entity_id}, Name: {self.name})"
