def am_gm_inequality(numbers: list[float]) -> float:
    product = 1
    n = len(numbers)
    for number in numbers:
        product *= number
    return product**(1/n)
