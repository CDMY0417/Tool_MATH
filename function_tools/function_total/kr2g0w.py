def calculate_total_cost(quantities: list[float], prices: list[float]) -> float:
    return sum(q * p for q, p in zip(quantities, prices))
