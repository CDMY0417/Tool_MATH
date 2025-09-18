def convert_to_decimal(numerator: int, denominator: int) -> str:
    decimal_result = numerator / denominator
    return f'{decimal_result:.{int(denominator).bit_length() - 1}f}'
