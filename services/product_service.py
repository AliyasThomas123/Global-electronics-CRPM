from repository.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def add_product(name, price, stock):
        if not name or price <= 0 or stock < 0:
            raise ValueError("Invalid product details.")
        ProductRepository.add_product(name, price, stock)
    
    @staticmethod
    def get_all_products():
        products = ProductRepository.get_all_products()
        return [{"Product ID": p[0], "Name": p[1], "Price": p[2], "Stock": p[3]} for p in products]
    
    @staticmethod
    def update_stock(product_id, stock_change):
        ProductRepository.update_stock(product_id, stock_change)
