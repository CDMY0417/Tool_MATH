def get_element_in_periodic_sequence(n: int, period: int, sequence: list):
    return sequence[(n - 1) % period]
