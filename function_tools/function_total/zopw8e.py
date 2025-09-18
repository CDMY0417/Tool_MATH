def solve_for_first_term(sequence_sum: int, last_term: int, number_of_terms: int) -> int:
    average_term = sequence_sum // number_of_terms
    first_term = (2 * average_term) - last_term
    return first_term
