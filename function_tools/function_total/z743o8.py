def digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(number))
