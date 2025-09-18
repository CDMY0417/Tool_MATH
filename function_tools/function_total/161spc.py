def collect_polynomial_terms(terms1: tuple, terms2: tuple):
    return tuple([t1 + t2 for t1, t2 in zip(terms1, terms2)])
