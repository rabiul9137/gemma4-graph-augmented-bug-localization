from inventory import check_stock

def place_order(product_id, quantity):
    if not check_stock(product_id, quantity):
        return "Out of stock"

    return "Order successful"
