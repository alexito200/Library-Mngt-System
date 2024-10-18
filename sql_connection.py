# sql_connection.py
import mysql.connector

def connect_database():
    conn = mysql.connector.connect(
        host="127.0.0.1",      # Update with your database host
        user="root",           # Update with your database username
        password="Vitoria96!",  # Update with your database password
        database="test_db"  # Update with your database name
    )
    return conn


    # try:
    #     connection = mysql.connector.connect(
    #         host="127.0.0.1",      # Update with your database host
    #         user="root",           # Update with your database username
    #         password="Vitoria96!",  # Update with your database password
    #         database="test_db"  # Update with your database name
    #     )
    #     if connection.is_connected():
    #         print("Successfully connected to the database.")
    #         return connection
    # except Error as e:
    #     print(f"Error: {e}")
    #     return None

