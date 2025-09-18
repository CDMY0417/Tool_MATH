def line_segment_fraction_point(A: tuple, B: tuple, m: float, n: float) -> tuple:
    x = (m * B[0] + n * A[0]) / (m + n)
    y = (m * B[1] + n * A[1]) / (m + n)
    return (x, y)
