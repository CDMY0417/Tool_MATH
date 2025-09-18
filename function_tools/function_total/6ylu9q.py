def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))
