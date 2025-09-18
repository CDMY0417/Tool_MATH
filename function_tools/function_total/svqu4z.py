def product_of_list(lst: list[float]) -> float:
    product = 1
    for number in lst:
        product *= number
    return product
