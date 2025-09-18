def largest_common_term_below_limit(base_term: int, common_difference: int, limit: int):
    m = (limit - base_term) // common_difference
    return base_term + common_difference * m
