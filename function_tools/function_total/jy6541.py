def sum_carry_value(values: list[int], carry: int, target: int) -> bool:
    return sum(values) + carry == target
