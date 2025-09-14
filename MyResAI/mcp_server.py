import sqlite3
from fastapi import FastAPI

# Create a FastAPI application instance
app = FastAPI()

DATABASE_PATH = 'MyResAI/myresai_database.db'

def get_menu_from_db():
    """
    Connects to the database and fetches all menu items.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    # This makes the results come back as dictionary-like rows
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, price, category, description FROM menu_items")
    menu_items = cursor.fetchall()
    
    conn.close()
    # Convert row objects to dictionaries for JSON serialization
    return [dict(item) for item in menu_items]

# --- API Endpoints ---

@app.get("/")
def read_root():
    """
    A simple root endpoint to confirm the server is running.
    """
    return {"status": "MyResAI MCP Server is running"}

@app.get("/menu")
def get_menu():
    """
    API endpoint to get the full restaurant menu.
    """
    menu_data = get_menu_from_db()
    return {"menu": menu_data}

# To run this server:
# 1. Make sure your virtual environment is active.
# 2. In your terminal, run the following command:
#    uvicorn MyResAI.mcp_server:app --reload
