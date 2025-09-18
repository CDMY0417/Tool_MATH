def law_of_cosines(side_opposite: int, side_adjacent1: int, side_adjacent2: int) -> float:
    return (side_adjacent1**2 + side_adjacent2**2 - side_opposite**2) / (2 * side_adjacent1 * side_adjacent2)
