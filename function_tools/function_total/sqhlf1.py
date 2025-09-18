def find_integers_in_interval(lower_bound: float, upper_bound: float):
    return [i for i in range(int(lower_bound) + 1, int(upper_bound) + 1) if lower_bound < i < upper_bound]
