from repository.database import get_connection

class CustomerRepository:
    @staticmethod
    def add_customer(name, email, phone):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            conn.commit()
            conn.close
            return f"Succesfully Registered {name}"
        except Exception as e:
            conn.rollback()  
      
            if 'UNIQUE constraint failed: Customers.email' in str(e):
                return  "This email is already registered. Please use a different email"
        conn.close()
    
    @staticmethod
    def get_all_customers():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customers WHERE is_active = 1")
        customers = cursor.fetchall()
        conn.close()
        return customers
    @staticmethod
    def deactivate_customer(customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Customers SET is_active = 0 WHERE customer_id = ?", (customer_id,))
        conn.commit()
        conn.close()
