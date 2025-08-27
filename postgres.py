import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        # Replace with your connection parameters
        connection = psycopg2.connect(
            host="localhost",
            database="db-k",
            user="postgres",
            password="postgres",
            port="5432"
        )
        
        # Test the connection by executing a simple query
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("PostgreSQL version:", db_version)
        
        # Close the connection
        cursor.close()
        connection.close()
        
        print("Connection successful!")
        return True
        
    except OperationalError as e:
        print(f"Connection failed: {e}")
        return False

# Test the connection
test_connection()