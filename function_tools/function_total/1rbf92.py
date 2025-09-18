def is_geometric_sequence(digits: list[int], r: float) -> bool:
    if len(digits) != 3:
        return False
    return digits[1] == digits[0] * r and digits[2] == digits[1] * r
