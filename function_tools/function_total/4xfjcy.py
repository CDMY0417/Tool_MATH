def calculate_expression_sign_changes(numerator_factors: list[float], denominator_factors: list[float]) -> list[tuple]:
    critical_points = sorted(numerator_factors + denominator_factors)
    intervals = []
    sign = 1  # Start with positive sign based on x=0 observation
    last_point = float('-inf')
    for point in critical_points:
        if sign > 0:
            intervals.append((last_point, point))
        sign *= -1  # Expression changes sign at each critical point
        last_point = point
    intervals.append((last_point, float('inf')))
    return intervals
