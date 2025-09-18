def count_integers_with_given_digit_length(digit_length: int, start: int, end: int) -> int:
    if digit_length == 1:
        return max(0, min(end, 9) - max(start, 1) + 1)
    if digit_length > 1:
        lower_bound = 10**(digit_length - 1)
        upper_bound = 10**digit_length - 1
        return max(0, min(upper_bound, end) - max(lower_bound, start) + 1)
    return 0
