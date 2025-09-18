def sum_of_digits(num: int) -> int:
    return sum(int(digit) for digit in str(num))
