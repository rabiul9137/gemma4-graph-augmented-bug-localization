
from pricing import calculate_total
from discounts import get_discount

def place_order(product_id, quantity, coupon):
    unit_price = {"BOOK": 100}.get(product_id, 0)
    discount_rate = get_discount(coupon)

    return calculate_total(
        unit_price, quantity, discount_rate
    )
