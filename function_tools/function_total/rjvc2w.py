def largest_integer_less_than(number: float) -> int:
    return int(number) if number == int(number) else int(number) - 1
