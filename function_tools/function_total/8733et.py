def find_common_denominator(denominators: list[int]) -> int:
    from sympy import lcm
    return lcm(denominators)
