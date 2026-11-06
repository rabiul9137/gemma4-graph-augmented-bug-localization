from validation import validate_quantity

def place_order(quantity):
    if not validate_quantity(quantity):
        return "Invalid quantity"

    return "Order accepted"
