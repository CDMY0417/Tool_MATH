def convert_base_to_decimal(number: str, base: int) -> int:
    total = 0
    power = len(number) - 1
    for digit in number:
        total += int(digit) * (base ** power)
        power -= 1
    return total
