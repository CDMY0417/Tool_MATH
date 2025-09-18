def sum_of_arithmetic_sequence(first_term: int, common_difference: int, number_of_terms: int) -> int:
    return number_of_terms * (2 * first_term + (number_of_terms - 1) * common_difference) // 2
