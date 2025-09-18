def convert_decimal_to_base(number: int, base: int) -> str:
    if number == 0:
        return '0'
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(str(x) for x in digits[::-1])
