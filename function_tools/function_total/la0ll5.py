def convert_base_representation(expanded_form: list[int], base: int) -> int:
    result = 0
    for power, coefficient in enumerate(expanded_form[::-1]):
        result += coefficient * (base ** power)
    return result
