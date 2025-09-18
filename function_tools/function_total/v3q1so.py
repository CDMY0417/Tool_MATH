def vertex_form_to_standard_form(a: float, h: float, k: float):
    x_squared_coefficient = a
    x_coefficient = -2 * a * h
    constant_term = a * h**2 + k
    return (x_squared_coefficient, x_coefficient, constant_term)
