def combine_like_terms(terms: list[str]) -> list[str]:
    from collections import defaultdict
    combined = defaultdict(int)
    for term in terms:
        coefficient, variable = term.split()
        combined[variable] += int(coefficient)
    return [f'{v}{k}' for k, v in combined.items()]
