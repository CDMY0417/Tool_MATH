def has_triangle_property(subset: list[int]) -> bool:
    from itertools import combinations
    for a, b, c in combinations(subset, 3):
        if a + b > c and a + c > b and b + c > a:
            return True
    return False
