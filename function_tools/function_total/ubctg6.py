def filter_positive_real_roots(roots: list[complex]) -> list[complex]:
    return [root for root in roots if root.real > 0]
