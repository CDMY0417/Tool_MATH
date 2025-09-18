def square_root_product(numbers: tuple[float, ...]) -> float:
    from math import sqrt
    product = 1
    for number in numbers:
        product *= number
    return sqrt(product)
