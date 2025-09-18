def count_choices_excluding(elements: list, excluded_set: set) -> int:
    return len([e for e in elements if e not in excluded_set])
