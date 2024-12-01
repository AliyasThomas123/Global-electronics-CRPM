import sqlite3

def get_connection():
    conn = sqlite3.connect("crpm_system.db")
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Customers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL,
        is_active BOOLEAN DEFAULT 1
    )
    """)
    
    # Products Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        is_active BOOLEAN DEFAULT 1
    )
    """)
    
    # Purchases Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Purchases (
        purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER NOT NULL,
        total_cost REAL NOT NULL,
        purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    )
    """)
    
    conn.commit()
    conn.close()
