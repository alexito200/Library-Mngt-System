# sql_connection.py
import mysql.connector

def connect_database():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Vitoria96!",
        database="test_db"
    )
    return conn