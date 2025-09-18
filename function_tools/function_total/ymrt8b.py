def largest_multiple_less_than(base: int, limit: int) -> int:
    quotient = limit // base
    return base * quotient
