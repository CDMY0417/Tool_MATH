def calculate_cosine_law(a_squared: float, b_squared: float, c_squared: float):
    from math import sqrt
    return (a_squared + b_squared - c_squared) / (2 * sqrt(a_squared) * sqrt(b_squared))
