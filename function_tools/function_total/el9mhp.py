def units_digit_of_product(numbers: list[int]) -> int:
    product = 1
    for num in numbers:
        product *= num
    return product % 10
