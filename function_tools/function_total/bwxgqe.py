def cosine_double_angle_solutions(k: int, value: float, theta_range: tuple):
    from math import cos, radians
    solutions = []
    for i in range(int(theta_range[0]), int(theta_range[1]) + 1):
        if cos(radians(k * i)) == value:
            solutions.append(i)
    return solutions
