def absolute_difference_zero_solutions(a: int, b: int, c: int, d: int) -> list:
    solutions = []
    # Case 1: a*x + b = c*x + d
    num1, den1 = b - d, a - c
    if den1 != 0:
        solutions.append(num1 / den1)
    # Case 2: a*x + b = -(c*x + d)
    num2, den2 = b + d, a + c
    if den2 != 0:
        solutions.append(num2 / den2)
    return solutions
