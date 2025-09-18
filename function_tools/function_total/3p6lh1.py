def count_non_zero_decimal_digits(num: int, denom: int) -> int:
    result = num / denom
    decimal_part = str(result).split('.')[-1]
    return sum(1 for digit in decimal_part if digit != '0')
