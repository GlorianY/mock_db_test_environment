import pandas as pd
from psycopg2 import connect
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from app.config import DB_USER, DB_PASSWORD

def create_pg_engine() -> Engine: 
    """Create Postgres engine."""
    PG_HOST = "db" # points to the DB container name
    PG_USER = DB_USER
    PG_PASSWORD = DB_PASSWORD
    PG_PORT = "5432"
    PG_DB_NAME = "postgres"

    # Create the connection
    engine = create_engine(f"postgresql://{PG_USER}:{DB_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB_NAME}")

    return engine


def get_product_by_brand(brand:str) -> pd.DataFrame:
    """Get all product data which belong to a specified brand."""
    engine = create_pg_engine()
    
    #df = pd.read_sql_query(f"SELECT * FROM product WHERE brand = {brand}",
    #                       engine)
    df = pd.read_sql_query(f"SELECT * FROM product",
                           engine)

    return df