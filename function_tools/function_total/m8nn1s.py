def largest_multiple_less_than(multiple_of: int, limit: int) -> int:
    largest = (limit // multiple_of) * multiple_of
    return largest
