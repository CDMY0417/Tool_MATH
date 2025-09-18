def rational_root_candidates(constant_factors: list[int], leading_factors: list[int]):
    candidates = set()
    for a in constant_factors:
        for b in leading_factors:
            candidates.add(a / b)
            candidates.add(-a / b)
    return list(candidates)
