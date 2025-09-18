def generate_arithmetic_sequence(start: int, difference: int, count: int) -> list:
    return [start + i * difference for i in range(count)]
