def product_of_list(numbers: list[int]) -> int:
    product = 1
    for num in numbers:
        product *= num
    return product
