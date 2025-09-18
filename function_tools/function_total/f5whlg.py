def largest_multiple_less_than(multiple: int, limit: int) -> int:
    quotient = limit // multiple
    return multiple * quotient
