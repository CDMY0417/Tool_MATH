def solve_ratio_equation(ratios: list[float], total_sum: float) -> float:
    x_coefficient = sum(ratios)
    return total_sum / x_coefficient
