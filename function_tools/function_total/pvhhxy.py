def is_perfect_cube_in_range(n: int, lo: int, hi: int) -> bool:
    cube = n**3
    return lo <= cube <= hi
