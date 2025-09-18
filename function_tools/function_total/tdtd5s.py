def match_coefficients(lhs_coeffs: tuple, rhs_coeffs: tuple) -> dict:
    matched = {}
    for i, (l, r) in enumerate(zip(lhs_coeffs, rhs_coeffs)):
        if l != r:
            matched[f'c{i}'] = r - l
    return matched
