def choose_ways(choices: list[int]) -> int:
    total_ways = 1
    for choice in choices:
        total_ways *= choice
    return total_ways
