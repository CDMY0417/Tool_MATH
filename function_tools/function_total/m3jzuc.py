def divisor_of_polynomial(coefficients: list[int], divisor_constant: int) -> list[int]:
    quotient = []
    remainder = coefficients[0]
    for coeff in coefficients[1:]:
        quotient.append(remainder)
        remainder = remainder * divisor_constant + coeff
    quotient.append(remainder)
    return quotient[:-1]
