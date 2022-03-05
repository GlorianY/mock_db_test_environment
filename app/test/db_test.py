import pandas as pd
from app.utils.db import get_product_by_brand


def test_get_product_by_brand():
    """Test get_product_by_brand() function."""
    expected = pd.DataFrame(
        [
            {
                "product_id": 1,
                "name": "Lenovo PC 1",
                "brand": "Lenovo",
                "description": "A regular Lenovo PC.",
                "price": 500,
            },
            {
                "product_id": 2,
                "name": "Lenovo PC 2",
                "brand": "Lenovo",
                "description": "A regular Lenovo PC 2.",
                "price": 550,
            },
            {
                "product_id": 3,
                "name": "Lenovo PC 3",
                "brand": "Lenovo",
                "description": "A regular Lenovo PC 3.",
                "price": 600,
            },
        ]
    )

    result = get_product_by_brand(brand="Lenovo")

    assert expected.equals(result)
