def probability_of_heads_and_tails(n_heads: int, n_tails: int, p_head: float, p_tail: float) -> float:
    return (p_head ** n_heads) * (p_tail ** n_tails)
