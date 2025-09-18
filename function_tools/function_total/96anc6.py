def inclusion_exclusion_principle(total: int, count_a: int, count_b: int, count_ab: int) -> int:
    return total - (count_a + count_b) + count_ab
