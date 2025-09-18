def distribute_term(term: int, expressions: list[int]) -> list[int]:
    return [term * expr for expr in expressions]
