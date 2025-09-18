def convert_to_base(number: int, base: int) -> list:
    if number == 0: return [0]
    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return digits[::-1]
