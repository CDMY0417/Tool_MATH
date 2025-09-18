def sum_digits_in_number(number: int) -> int:
    return sum(int(digit) for digit in str(number))
