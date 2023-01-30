from menu import products
from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(28))
    print(get_products_by_type('drink'))
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product(products, **new_product))
