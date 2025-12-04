import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="@bhishekMa1i",
        database="testdb"
    )
    return db
