def rational_root_candidates(leading_coefficient: int, constant_term: int):
    from itertools import product
    def factors(n):
        return set(x for tup in ((i, n//i) for i in range(1, int(abs(n)**0.5) + 1) if n % i == 0) for x in tup)
    p_factors = factors(constant_term)
    q_factors = factors(leading_coefficient)
    return set(fp / fq for fp, fq in product(p_factors, q_factors)).union(set(-fp / fq for fp, fq in product(p_factors, q_factors)))
