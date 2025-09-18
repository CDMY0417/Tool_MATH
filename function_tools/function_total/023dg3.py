def add_equations(equation1: tuple, result1: int, equation2: tuple, result2: int):
    return tuple(c1 + c2 for c1, c2 in zip(equation1, equation2)), result1 + result2
