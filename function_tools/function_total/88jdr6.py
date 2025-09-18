def convert_to_base_12(number: int) -> list[int]:
    if number == 0:
        return [0]
    digits = []
    while number > 0:
        digits.append(number % 12)
        number //= 12
    return digits[::-1]
