def product_of_digits(digits: list[int]) -> int:
    product = 1
    for digit in digits:
        product *= digit
    return product
