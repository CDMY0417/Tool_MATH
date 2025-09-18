def next_multiple_greater_than(number: int, base: int) -> int:
    if number % base == 0:
        return number
    return (number // base + 1) * base
