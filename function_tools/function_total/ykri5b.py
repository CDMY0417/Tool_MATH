def equation_of_circle(x_part: str, y_part: str, constant: int):
    h = -int(x_part.split('+')[1])
    k = -int(y_part.split('+')[1])
    r = int(constant ** 0.5)
    return ((h, k), r)
