from repository.customer_repository import CustomerRepository

class CustomerService:
    @staticmethod
    def add_customer(name, email, phone):
        if not name or not email or not phone:
            raise ValueError("All fields are required.")
        CustomerRepository.add_customer(name, email, phone)
    
    @staticmethod
    def get_all_customers():
        customers = CustomerRepository.get_all_customers()
        return [{"Customer ID": c[0], "Name": c[1], "Email": c[2], "Phone": c[3]} for c in customers]
    
    @staticmethod
    def deactivate_customer(customer_id):
        CustomerRepository.deactivate_customer(customer_id)
