def complementary_probability(total_outcomes: int, unfavorable_outcomes: int) -> float:
    favorable_outcomes = total_outcomes - unfavorable_outcomes
    return favorable_outcomes / total_outcomes
