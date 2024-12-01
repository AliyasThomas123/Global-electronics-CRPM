from repository.database import get_connection

class ProductRepository:
    @staticmethod
    def add_product(name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        try : 
            cursor.execute("INSERT INTO Products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
            conn.commit()
            conn.close
            return f"Product {name} added Succesfully !"
        except Exception as e:
            conn.rollback()
            print(f'EXCEPTION------>{e}')
            return 'Unable to Add product !'
        conn.close()
    
    @staticmethod
    def get_all_products():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE is_active = 1")
        products = cursor.fetchall()
        conn.close()
        return products
    @staticmethod
    def update_stock(product_id, stock_change):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Products SET stock = stock + ? WHERE product_id = ?", (stock_change, product_id))
        conn.commit()
        conn.close()
