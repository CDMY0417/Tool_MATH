def polynomial_long_division(dividend: list[float], divisor: list[float]) -> list[float]:
    while len(dividend) >= len(divisor):
        scale_factor = dividend[0] / divisor[0]
        subtracted_polynomial = [scale_factor * term for term in divisor] + [0] * (len(dividend) - len(divisor))
        dividend = [a - b for a, b in zip(dividend, subtracted_polynomial)]
        while dividend and dividend[0] == 0:
            dividend.pop(0)
    return dividend
