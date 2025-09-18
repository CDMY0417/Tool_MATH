def sum_of_arithmetic_sequence(first_term: int, common_difference: int, n_terms: int):
    last_term = first_term + (n_terms - 1) * common_difference
    return n_terms * (first_term + last_term) // 2
