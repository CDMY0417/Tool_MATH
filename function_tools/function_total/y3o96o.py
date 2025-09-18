def sum_of_geometric_series(a: int, r: int, n: int) -> int:
    return (a * r**n - a) // (r - 1)
