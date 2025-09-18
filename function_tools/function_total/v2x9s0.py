def calculate_period_sum(sequence: list[int], total_length: int) -> int:
    period_length = len(sequence)
    full_periods = total_length // period_length
    remaining_terms = total_length % period_length
    return full_periods * sum(sequence) + sum(sequence[:remaining_terms])
