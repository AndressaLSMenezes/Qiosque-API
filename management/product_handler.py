from menu import products


def get_product_by_id(product_id):
    try:
        for product in products:
            if product["_id"] == product_id:
                return product
        return {}
    except ValueError:
        print("O id é invalido")


def get_products_by_type(type):
    try:
        list_products = []
        for product in products:
            if product["type"] == type:
                list_products.append(product)
        return list_products
    except ValueError:
        print("O tipo não existe")


def add_product(list, **product):
    product["_id"] = len(list) + 1
    list.append(product)
    return product
