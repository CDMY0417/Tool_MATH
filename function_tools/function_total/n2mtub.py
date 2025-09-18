def product_of_sequence(sequence: list[float]) -> float:
    product = 1
    for number in sequence:
        product *= number
    return product
