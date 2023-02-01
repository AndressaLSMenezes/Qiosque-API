from menu import products


def get_product_by_id(product_id):
    if type(product_id) is not int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == product_id:
            return product
    return {}


def get_products_by_type(type_product):
    if type(type_product) is not str:
        raise TypeError("product type must be a str")
    list_products = []
    for product in products:
        if product["type"] == type_product:
            list_products.append(product)
    return list_products


def add_product(list, **product):
    id = 0
    for itens in list:
        if itens["_id"] > id:
            id = itens["_id"]
    product["_id"] = id + 1
    list.append(product)
    return product


def menu_report():
    count_product = len(products)
    total_price = 0
    type_exists = []
    repeated_type = []
    count_type = 0
    common_type = ""
    for product in products:
        total_price = total_price + product["price"]
        if product["type"] not in type_exists:
            type_exists.append(product["type"])
        else:
            repeated_type.append(product["type"])
    for type_name in type_exists:
        type_test = repeated_type.count(type_name)
        if type_test > count_type:
            count_type = type_test
            common_type = type_name
    return f"Products Count: {count_product} - Average Price: ${round(total_price/count_product, 2)} - Most Common Type: {common_type}"
