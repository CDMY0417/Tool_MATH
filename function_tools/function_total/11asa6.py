def sum_of_positive_integers(conditions: list[bool]) -> int:
    return sum([i + 1 for i, condition in enumerate(conditions) if condition])
