def vieta_formulas_cubic(coefficients: tuple):
    a, b, c, d = coefficients
    sum_roots = -b / a
    sum_product_roots = c / a
    product_roots = -d / a
    return sum_roots, sum_product_roots, product_roots
