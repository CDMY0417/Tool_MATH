def find_integer_pair_with_product_sum(product: int, difference: int) -> tuple:
    for i in range(1, int(product**0.5) + 1):
        if product % i == 0:
            j = product // i
            if abs(j - i) == difference:
                return (i, j)
    return ()
