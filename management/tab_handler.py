from menu import products


def calculate_tab(list):
    product_value = 0
    for item in list:
        for product in products:
            if product["_id"] == item["_id"]:
                vari = product["price"] * item["amount"]
                product_value = product_value + vari
                break
    return {'subtotal': f'${round(product_value, 2)}'}
