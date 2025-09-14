
import sqlite3

DB_FILE = "MyResAI/myresai_database.db"

def setup_database():
    """
    Creates and sets up the SQLite database with the necessary tables and sample data.
    """
    # Connect to the database (this will create the file if it doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # --- Create Tables ---

    # Customer Information
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT UNIQUE,
        email TEXT
    )
    ''')

    # Menu Items
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category TEXT
    )
    ''')

    # Order History
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_amount REAL,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
    ''')
    
    # Order Details (links orders to menu items)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        menu_item_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (menu_item_id) REFERENCES menu_items (id)
    )
    ''')

    # Table Reservations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        reservation_time TIMESTAMP NOT NULL,
        number_of_guests INTEGER,
        table_number INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
    ''')
    
    # --- Insert Sample Data (if tables are empty) ---
    
    # Check if customers table is empty before inserting
    cursor.execute("SELECT COUNT(*) FROM customers")
    if cursor.fetchone()[0] == 0:
        print("Inserting sample customer data...")
        sample_customers = [
            ('Sriram', '1234567890', 'sriram@example.com'),
            ('Priya', '0987654321', 'priya@example.com')
        ]
        cursor.executemany("INSERT INTO customers (name, phone_number, email) VALUES (?, ?, ?)", sample_customers)

    # For the menu, we will clear and re-insert every time to ensure it's up-to-date.
    print("Clearing old menu and inserting updated sample menu data...")
    cursor.execute("DELETE FROM menu_items")
    
    sample_menu = [
        # Breakfast
        ('Idli (2 pcs)', 'Steamed rice cakes served with chutney and sambar', 40.00, 'Breakfast'),
        ('Dosa', 'Crispy rice and lentil crepe', 60.00, 'Breakfast'),
        ('Masala Dosa', 'Dosa filled with spiced potatoes', 80.00, 'Breakfast'),
        ('Vada (2 pcs)', 'Fried lentil donuts', 50.00, 'Breakfast'),
        ('Upma', 'Savory semolina porridge', 45.00, 'Breakfast'),
        
        # Lunch & Dinner
        ('South Indian Thali', 'A complete meal with rice, sambar, rasam, curries, and dessert', 150.00, 'Lunch/Dinner'),
        ('Chicken Biryani', 'Aromatic rice dish with chicken', 220.00, 'Lunch/Dinner'),
        ('Vegetable Korma', 'Mixed vegetables in a creamy coconut gravy', 180.00, 'Lunch/Dinner'),
        ('Parotta with Salna', 'Layered flatbread with a spicy gravy', 90.00, 'Lunch/Dinner'),
        
        # Appetizers
        ('Samosa (2 pcs)', 'Spicy fried pastry', 30.00, 'Appetizer'),
        ('Gobi 65', 'Spicy deep-fried cauliflower florets', 120.00, 'Appetizer'),

        # Desserts
        ('Gulab Jamun', 'Sweet milk-solid dessert', 60.00, 'Dessert'),
        ('Payasam', 'Traditional South Indian pudding', 70.00, 'Dessert')
    ]
    cursor.executemany("INSERT INTO menu_items (name, description, price, category) VALUES (?, ?, ?, ?)", sample_menu)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database 'myresai_database.db' is set up and ready.")


if __name__ == "__main__":
    setup_database()
