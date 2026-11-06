
def calculate_total(unit_price, quantity, discount_rate):
    subtotal = unit_price * quantity
    discount = subtotal * discount_rate
    return subtotal - discount
