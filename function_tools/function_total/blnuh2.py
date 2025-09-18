def product_of_digits(number: int) -> int:
    product = 1
    while number > 0:
        product *= number % 10
        number //= 10
    return product
