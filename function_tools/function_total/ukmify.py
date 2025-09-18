def product_modulo(numbers: list[int], mod: int) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product % mod
