def total_outcomes(outcomes_per_event: list[int]) -> int:
    total = 1
    for outcomes in outcomes_per_event:
        total *= outcomes
    return total
