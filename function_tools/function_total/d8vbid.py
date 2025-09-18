def filter_two_digit_numbers(numbers: set[int]) -> set[int]:
    return {x for x in numbers if 10 <= x <= 99}
