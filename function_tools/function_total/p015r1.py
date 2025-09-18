def choices_for_digit(position: int, total_digits: int):
    if position == 0:
        return 9
    if position < (total_digits + 1) // 2:
        return 10
    return 0
