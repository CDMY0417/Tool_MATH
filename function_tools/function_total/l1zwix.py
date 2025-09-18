def sum_roots_geometric_progression(first_term: float, common_ratio: float):
    return first_term * (1 / common_ratio**2 + 1 / common_ratio + 1 + common_ratio + common_ratio**2)
