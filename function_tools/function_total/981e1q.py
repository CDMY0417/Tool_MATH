def is_affordable(item_prices: list[float], budget: float) -> bool:
    return sum(item_prices) <= budget
