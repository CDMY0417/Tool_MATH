def modular_product(numbers: list[int], m: int) -> int:
    product = 1
    for number in numbers:
        product = (product * number) % m
    return product
