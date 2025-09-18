def calculate_percent_error(actual: float, estimated: float) -> float:
    return abs((actual - estimated) / actual) * 100
