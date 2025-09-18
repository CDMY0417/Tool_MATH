def possible_rational_roots(constant_divisors: set, leading_divisors: set):
    possible_roots = set()
    for a in constant_divisors:
        for b in leading_divisors:
            possible_roots.add(a / b)
            possible_roots.add(-a / b)
    return possible_roots
