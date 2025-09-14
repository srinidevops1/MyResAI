import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from fastapi.testclient import TestClient
from MyResAI.mcp_server import app

from MyResAI.database_setup import setup_database, DB_FILE

# Ensure the database and tables exist before running API tests
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
setup_database()

# Ensure the database and tables exist before running API tests
setup_database()

# Create a test client for our FastAPI app
client = TestClient(app)


def test_read_root():
    """
    Tests the root endpoint ('/').
    It should return a 200 OK status and a specific JSON message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "MyResAI MCP Server is running"}

def test_get_menu():
    """
    Tests the menu endpoint ('/menu').
    It should return a 200 OK status and the menu data.
    """
    response = client.get("/menu")
    assert response.status_code == 200
    
    data = response.json()
    # Check that the response has a "menu" key
    assert "menu" in data
    # Check that the menu is a list (even if it's empty)
    assert isinstance(data["menu"], list)
    
    # If the menu is not empty, check the structure of the first item
    if len(data["menu"]) > 0:
        first_item = data["menu"][0]
        assert "name" in first_item
        assert "price" in first_item
        assert "category" in first_item
