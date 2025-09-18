def count_combinations(letter_count: int, digit_count: int) -> int:
    return (26 ** letter_count) * (10 ** digit_count)
