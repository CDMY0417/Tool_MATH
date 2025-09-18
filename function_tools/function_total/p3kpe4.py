def rational_root_candidates(constant_divisors: list[int], leading_coefficient_divisors: list[int]) -> list[float]:
    candidates = set()
    for a in constant_divisors:
        for b in leading_coefficient_divisors:
            candidates.add(a / b)
            candidates.add(-a / b)
    return sorted(candidates)
