def product_of_digits(number: int) -> int:
    from functools import reduce
    from operator import mul
    if number == 0:
        return 0
    digits = [int(digit) for digit in str(abs(number))]
    return reduce(mul, digits, 1)
