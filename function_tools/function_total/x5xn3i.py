def find_possible_y_values(min_y: float, max_y: float, step: float):
    y_values = []
    current_y = min_y
    while current_y < max_y:
        if (2 * current_y).is_integer():
            y_values.append(current_y)
        current_y += step
    return y_values
