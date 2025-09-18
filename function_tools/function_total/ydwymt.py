def compute_periodic_sequence_value(n: int, initial_values: list[int], period: int):
    return initial_values[(n - 1) % period]
