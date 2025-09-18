def factor_out_gcd_from_terms(terms: list[int], gcd: int) -> list[int]:
    return [term // gcd for term in terms]
