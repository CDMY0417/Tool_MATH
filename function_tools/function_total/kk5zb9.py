def apply_discount(price: float, discount_percent: float) -> float:
    return price * ((100 - discount_percent) / 100)
