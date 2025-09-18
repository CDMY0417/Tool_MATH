def product_of_numbers(numbers: list[float]) -> float:
    result = 1
    for number in numbers:
        result *= number
    return result
