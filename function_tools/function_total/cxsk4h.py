def is_arithmetic_sequence_odd(first_term: int, difference: int, terms_count: int) -> bool:
    return all((first_term + i * difference) % 2 != 0 for i in range(terms_count))
