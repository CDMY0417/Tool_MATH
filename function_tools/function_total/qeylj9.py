def apply_componendo_dividendo(num1: float, denom1: float, num2: float, denom2: float):
    numerator1 = num1 + denom1
    denominator1 = num1 - denom1
    numerator2 = num2 + denom2
    denominator2 = num2 - denom2
    return (numerator1 / denominator1, numerator2 / denominator2)
