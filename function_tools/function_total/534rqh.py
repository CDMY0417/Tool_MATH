def convert_to_base(number: int, base: int) -> list:
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    return digits[::-1]
