def list_values_less_than(a: int, b: int, limit: int):
    values = []
    x = 0
    current_value = a * x + b
    while current_value < limit:
        values.append(current_value)
        x += 1
        current_value = a * x + b
    return values
