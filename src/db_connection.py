import mysql.connector

def get_connection():
    """Establishes and returns a MySQL connection."""
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Safalya@7',
        database='MovieRecommendation'
    )
    return cnx
