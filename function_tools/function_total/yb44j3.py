def convert_to_base_b(number_str: str, base: int) -> int:
    result = 0
    power = len(number_str) - 1
    for digit in number_str:
        result += int(digit) * (base ** power)
        power -= 1
    return result
