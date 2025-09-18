def square_less_than_or_equal_to_self(values: list[float]) -> bool:
    return all(x ** 2 <= x for x in values)
