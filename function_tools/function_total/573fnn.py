def count_rational_roots(divisors_numerator: set, divisors_denominator: set) -> int:
    rational_roots = set()
    for numerator in divisors_numerator:
        for denominator in divisors_denominator:
            rational_roots.add(numerator / denominator)
    return len(rational_roots)
