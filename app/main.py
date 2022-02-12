from fastapi import FastAPI
from app.utils.db import get_product_by_name

app = FastAPI()


@app.get("/search_product/{product_name}")
def search_product(product_name:str) -> dict:

    result = get_product_by_name(product_name=product_name)
    return {

    }