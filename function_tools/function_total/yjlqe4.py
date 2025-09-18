def geometric_series_sum(first_term: int, ratio: int, num_terms: int) -> int:
    return first_term * (ratio ** num_terms - 1) // (ratio - 1)
