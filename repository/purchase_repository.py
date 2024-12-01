from repository.database import get_connection

class PurchaseRepository:
    @staticmethod
    def add_purchase(customer_id, product_id, quantity, total_cost):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Purchases (customer_id, product_id, quantity, total_cost)
        VALUES (?, ?, ?, ?)
        """, (customer_id, product_id, quantity, total_cost))
        res= cursor.execute("UPDATE Products SET stock = stock - ? WHERE product_id = ?", (quantity, product_id))
        conn.commit()
        conn.close()
        print("db",res)
    @staticmethod
    def get_sales_summary():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""

SELECT 
    products.name AS ProductName,
    SUM(purchases.quantity) AS TotalSales,
    SUM(purchases.quantity * products.price) AS Profit
FROM 
    purchases
JOIN 
    products ON purchases.product_id = products.product_id
GROUP BY 
    products.name;

                       """)
        summary = cursor.fetchall()
        conn.close()
        return summary

    @staticmethod
    def get_top_customers():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT customer_id, SUM(total_cost) as total_purchases 
        FROM Purchases 
        GROUP BY customer_id 
        ORDER BY total_purchases DESC
        """)
        customers = cursor.fetchall()
        conn.close()
        return customers

    @staticmethod
    def get_product_performance():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT p.product_id, p.name, SUM(pr.quantity) as total_sold 
        FROM Products p
        JOIN Purchases pr ON p.product_id = pr.product_id
        GROUP BY p.product_id
        ORDER BY total_sold DESC
        """)
        performance = cursor.fetchall()
        conn.close()
        return performance
    @staticmethod
    def get_all_purchases():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""

       SELECT 
    customers.customer_id,
    customers.name AS CustomerName,
    products.product_id,
    products.name AS ProductName,
    purchases.quantity,
    purchases.purchase_id                   
FROM 
    purchases
JOIN 
    customers ON purchases.customer_id = customers.customer_id
JOIN 
    products ON purchases.product_id = products.product_id; 
                       """)
        products = cursor.fetchall()
        conn.close()
        return products
