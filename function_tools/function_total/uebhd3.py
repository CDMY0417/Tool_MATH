def probability_two_cards(n_target: int, total: int) -> float:
    return (n_target / total) * ((n_target - 1) / (total - 1))
