"""
Creates and sets up the SQLite database with the necessary tables and sample data.
"""
# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect('MyResAI/myresai_database.db')
cursor = conn.cursor()

# --- Create Tables ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    room_id INTEGER,
    start_date TEXT,
    end_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (room_id) REFERENCES rooms (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT NOT NULL,
    room_type TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# --- Insert Sample Data ---
cursor.execute('''
INSERT INTO users (username, password, email) VALUES
('john_doe', 'password123', 'john@example.com'),
('jane_doe', 'password456', 'jane@example.com')
''')

cursor.execute('''
INSERT INTO rooms (room_number, room_type, price) VALUES
('101', 'Single', 100.00),
('102', 'Double', 150.00),
('103', 'Suite', 250.00)
''')

conn.commit()
conn.close()