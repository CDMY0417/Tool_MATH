def prod_of_squares_sqrt(factor_dict: dict):
    product = 1
    for prime, power in factor_dict.items():
        product *= prime ** (power // 2)
    return product
