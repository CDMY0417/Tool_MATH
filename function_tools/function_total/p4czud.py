def count_outcomes_with_condition(outcomes: list[str]) -> int:
    count = 0
    for outcome in outcomes:
        if outcome.count('H') >= outcome.count('T'):
            count += 1
    return count
