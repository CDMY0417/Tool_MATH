def cyclic_sequence_partial_sum(n: int, period_sum: int, partial_period_sum: int, extra_terms: int):
    full_periods_count = n // extra_terms
    sum_of_full_periods = full_periods_count * period_sum
    return sum_of_full_periods + partial_period_sum
