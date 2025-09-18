def count_possible_third_sides(equal_side: int, potential_third_sides: list[int]) -> int:
    max_third_side = 2 * equal_side
    count = 0
    for side in potential_third_sides:
        if side != equal_side and side < max_third_side:
            count += 1
    return count
