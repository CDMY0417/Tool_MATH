def find_two_numbers_with_sum(total: int, max_value: int, exclude_values: set):
    for x in range(max_value, 0, -1):
        y = total - x
        if y < max_value and y > 0 and x != y and x not in exclude_values and y not in exclude_values:
            return (x, y)
    return None
