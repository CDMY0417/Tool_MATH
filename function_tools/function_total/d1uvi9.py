def points_below_average(scores: list[int], average: int) -> int:
    return sum(max(0, average - score) for score in scores)
