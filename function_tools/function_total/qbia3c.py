def create_sign_chart(numerator_factors: list[float], denominator_factors: list[float]):
    import numpy as np
    critical_points = sorted(set(numerator_factors + denominator_factors))
    intervals = [(-np.inf, critical_points[0])] + [(critical_points[i], critical_points[i+1]) for i in range(len(critical_points)-1)] + [(critical_points[-1], np.inf)]
    sign_chart = []
    for inter in intervals:
        sample_point = (inter[0] + inter[1]) / 2
        sign = 1
        for factor in numerator_factors:
            if sample_point - factor < 0:
                sign *= -1
        for factor in denominator_factors:
            if sample_point - factor < 0:
                sign *= -1
        sign_chart.append(sign)
    return sign_chart
