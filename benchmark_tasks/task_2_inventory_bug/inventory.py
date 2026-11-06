def check_stock(product_id, quantity):
    stock = {"BOOK": 50}
    available = stock.get(product_id, 0)

    return available < quantity
