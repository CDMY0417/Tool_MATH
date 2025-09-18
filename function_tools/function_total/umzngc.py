def convert_to_base_3(number: int) -> list:
    base_3_digits = []
    while number > 0:
        base_3_digits.append(number % 3)
        number = number // 3
    return base_3_digits[::-1]
