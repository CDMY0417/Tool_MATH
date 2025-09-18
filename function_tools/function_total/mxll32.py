def evaluate_quadratic_factors(m: int, n: int):
    def sign(interval):
        test_value = m + interval[0] if m < n else n + interval[0]
        return (test_value + m) * (test_value + n) <= 0
    regions = [(-float('inf'), min(m, n)), (min(m, n), max(m, n)), (max(m, n), float('inf'))]
    results = [sign(interval) for interval in regions]
    return results
