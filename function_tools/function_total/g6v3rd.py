def solve_for_geometric_ratio(first_term: int, known_term: int, index_first: int, index_known: int) -> int:
    return int((known_term / first_term) ** (1 / (index_known - index_first)))
