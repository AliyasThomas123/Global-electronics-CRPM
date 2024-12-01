from repository.purchase_repository import PurchaseRepository
from repository.product_repository import ProductRepository
from repository.customer_repository import CustomerRepository

class PurchaseService:
    @staticmethod
    def record_purchase(customer_id, product_id, quantity):
        product = ProductRepository.get_product_by_id(product_id)
        if product is None or product["stock"] < quantity:
            raise ValueError("Insufficient stock or product not found.")
        
        total_cost = product["price"] * quantity
        PurchaseRepository.add_purchase(customer_id, product_id, quantity, total_cost)
        ProductRepository.update_stock(product_id, -quantity)
    
    @staticmethod
    def get_customer_purchases(customer_id):
        purchases = PurchaseRepository.get_purchases_by_customer(customer_id)
        return [
            {
                "Purchase ID": p[0],
                "Product ID": p[2],
                "Quantity": p[3],
                "Total Cost": p[4],
                "Date": p[5],
            }
            for p in purchases
        ]
