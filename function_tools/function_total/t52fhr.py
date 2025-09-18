def sum_of_consecutive_integers(start: int, end: int) -> int:
    return (end * (end + 1) // 2) - (start * (start - 1) // 2)
