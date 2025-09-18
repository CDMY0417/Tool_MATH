def probability_even_or_greater_than(total_numbers: int, cutoff: int, even_numbers: int) -> float:
    return (even_numbers + (total_numbers - cutoff + 1 - (even_numbers // 2) )) / total_numbers
