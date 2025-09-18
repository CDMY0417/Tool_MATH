def parameterize_line(b: tuple, dir_vec: tuple, t: float):
    return tuple(b[i] + t * dir_vec[i] for i in range(len(b)))
