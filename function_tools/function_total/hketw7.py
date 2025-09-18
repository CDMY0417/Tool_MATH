def distribute_terms(factor: str, terms: list[str]) -> list[str]:
    distributed = []
    for term in terms:
        distributed.append(f'{factor}*{term}')
    return distributed
