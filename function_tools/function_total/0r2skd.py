def divide_polynomials_synthetic(dividend: list[float], divisor: list[float]) -> tuple:
    out = list(dividend)
    normalizer = divisor[0]
    for i in range(len(dividend) - len(divisor) + 1):
        out[i] /= normalizer
        coef = out[i]
        if coef != 0:
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coef
    sep_index = -(len(divisor) - 1)
    return out[:sep_index], out[sep_index:]
