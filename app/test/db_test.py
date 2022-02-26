from app.utils.db import get_product_by_brand

def test_get_product_by_brand():
    """Test get_product_by_brand() function."""
    print(get_product_by_brand(brand="Lenovo"))
