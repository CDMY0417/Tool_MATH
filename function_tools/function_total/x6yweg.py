def expand_product(quadratic_coeffs: tuple, linear_coeffs: tuple):
    a_quad, b_quad, c_quad = quadratic_coeffs
    a_linear, b_linear = linear_coeffs
    a_result = a_quad * a_linear
    b_result = a_quad * b_linear + b_quad * a_linear
    c_result = b_quad * b_linear + c_quad * a_linear
    d_result = c_quad * b_linear
    return (a_result, b_result, c_result, d_result)
