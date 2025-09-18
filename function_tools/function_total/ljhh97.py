def sum_arithmetic_sequence_terms(first_term: int, num_terms: int, common_difference: int) -> int:
    last_term = first_term + (num_terms - 1) * common_difference
    return num_terms * (first_term + last_term) // 2
