def evaluate_polynomial(x: int, x_params: list[int], a: int):
    result = a
    for x_i in x_params:
        result *= (x - x_i)
    result += x**2 + 2
    return result
