def convert_to_base(number: int, base: int):
    digits = []
    while number > 0:
        digits.append(number % base)
        number //= base
    return digits[::-1]
