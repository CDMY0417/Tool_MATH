def subtract_equations(equation1: tuple, equation2: tuple):
    return tuple(e1 - e2 for e1, e2 in zip(equation1, equation2))
