import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import os
import sqlite3
import pytest
from MyResAI.database_setup import DB_FILE, setup_database

# Define the expected path for the test database
TEST_DB_PATH = 'MyResAI/myresai_database.db'


def cleanup_database():
    """Utility function to delete the database file if it exists."""
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)


def test_database_creation():
    """
    Tests if the database file is created by setup_database().
    """
    # Start with a clean slate
    cleanup_database()
    
    # Run the setup function
    setup_database()
    
    # Assert that the database file now exists
    assert os.path.exists(TEST_DB_PATH)
    
    # Clean up after the test
    cleanup_database()


def test_tables_are_created():
    """
    Tests if all the expected tables are created in the database.
    """
    # Start with a clean slate
    cleanup_database()
    
    # Run the setup function
    setup_database()
    
    # Connect to the newly created database
    conn = sqlite3.connect(TEST_DB_PATH)
    cursor = conn.cursor()
    
    # Get the list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    
    # Assert that all our expected tables are in the list
    expected_tables = ['customers', 'menu_items', 'orders', 'order_details', 'reservations']
    for table in expected_tables:
        assert table in tables
        
    # Clean up after the test
    cleanup_database()
