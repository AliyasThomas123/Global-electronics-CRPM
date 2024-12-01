from repository.customer_repository import CustomerRepository
from repository.product_repository import ProductRepository
from repository.purchase_repository import PurchaseRepository
from models.customer import Customer
from models.product import Product
from models.purchase import Purchase

class EntityService:
    @staticmethod
    def add_entity(entity):
        if isinstance(entity, Customer):
            res=CustomerRepository.add_customer(entity.name, entity.email, entity.phone)
        elif isinstance(entity, Product):
            res=ProductRepository.add_product(entity.name, entity.price, entity.stock)
        elif isinstance(entity, Purchase):
            res=PurchaseRepository.add_purchase(
                entity.customer_id, entity.product_id, entity.quantity, entity.total_cost
            )
        
        else:
            raise TypeError("Unsupported entity type.")
        if res:
            return res   
