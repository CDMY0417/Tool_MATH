def multiply_quadratics(quadratic1: tuple, quadratic2: tuple):
    a1, b1, c1 = quadratic1
    a2, b2, c2 = quadratic2
    return (a1*a2, a1*b2 + b1*a2, a1*c2 + b1*b2 + c1*a2, b1*c2 + c1*b2, c1*c2)
