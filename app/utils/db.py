from psycopg2 import connect
from app.config import DB_USER, DB_PASSWORD

def get_product_by_name(product_name:str) -> TODO:
    # Connect to the database
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")    

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    cursor.execute(f"select * where brand = {product_name}")

    # Fetch result
        