def solve_for_y_in_standard_form(a: float, b: float, c: float) -> tuple:
    m = -a / b
    b_intercept = c / b
    return (m, b_intercept)
