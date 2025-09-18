def apply_discount(original_price: float, discount_percentage: float) -> float:
    return original_price * (1 - discount_percentage / 100)
