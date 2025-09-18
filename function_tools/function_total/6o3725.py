def calculate_combinations(groups: list[int]) -> int:
    total = 1
    for group_size in groups:
        total *= group_size
    return total
