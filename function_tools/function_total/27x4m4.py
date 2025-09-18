def change_of_base_log(a: float, b: float, x: float):
    from math import log
    return log(x) / log(a), log(x) / log(b)
