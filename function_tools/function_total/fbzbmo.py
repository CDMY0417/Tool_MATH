def nth_number_with_digit_length(n: int, digit_length: int):
    start_number = 10**(digit_length - 1)
    return start_number + n - 1
