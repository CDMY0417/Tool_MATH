def sum_of_digits(decimal_number: str, n: int) -> int:
    digits = decimal_number.replace('0.', '').replace('\overline', '')[:n]
    return sum(int(d) for d in digits)
