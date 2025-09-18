def product_of_absolute_values(complex_numbers: list[complex]) -> float:
    product = 1
    for num in complex_numbers:
        product *= abs(num)
    return product
