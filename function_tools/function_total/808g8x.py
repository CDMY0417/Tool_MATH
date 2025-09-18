def compute_p_value(q_value: float, x_value: float):
    return (q_value + x_value) / (x_value**2 - 1)
