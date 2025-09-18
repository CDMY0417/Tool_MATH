def divide_by_identical_items(arrangements: int, identical_count: int) -> int:
    from math import factorial
    return arrangements // factorial(identical_count)
