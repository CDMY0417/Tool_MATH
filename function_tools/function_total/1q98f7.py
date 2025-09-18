def smallest_exponent_exceeding_value(first_term: int, common_ratio: int, threshold: int) -> int:
    k = 0
    while first_term * common_ratio ** k <= threshold:
        k += 1
    return k
