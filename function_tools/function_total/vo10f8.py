def probability_choose_one_first(n_target: int, n_non_target: int, total: int) -> float:
    return (n_target / total) * (n_non_target / (total - 1))
