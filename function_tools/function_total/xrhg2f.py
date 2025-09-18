def square_root_interval(lo: float, hi: float):
    assert 0 < lo <= hi, "Interval must be positive and non-empty"
    from math import sqrt
    return (sqrt(lo), sqrt(hi))
