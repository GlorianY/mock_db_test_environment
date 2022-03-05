import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def create_pg_engine() -> Engine:
    """Create Postgres engine."""
    PG_HOST = os.environ["DB_HOST"]
    PG_USER = os.environ["DB_USER"]
    PG_PASSWORD = os.environ["DB_PASSWORD"]
    PG_PORT = os.environ["DB_PORT"]
    PG_DB_NAME = os.environ["DB_NAME"]

    # Create the connection
    engine = create_engine(
        f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB_NAME}"
    )

    return engine


def get_product_by_brand(brand: str) -> pd.DataFrame:
    """Get all product data which belong to a specified brand."""
    engine = create_pg_engine()

    df = pd.read_sql_query(f"SELECT * FROM product WHERE brand = '{brand}'", engine)

    return df
