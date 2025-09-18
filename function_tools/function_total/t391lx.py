def collect_like_terms(terms: list):
    from sympy import simplify
    return simplify(sum(terms))
