def roots_with_ratio(product: int, ratio_numerator: int, ratio_denominator: int) -> tuple:
    beta = product ** 0.5 * ratio_denominator**0.5 / (ratio_numerator * ratio_denominator)**0.5
    alpha = ratio_numerator * beta / ratio_denominator
    return alpha, beta
