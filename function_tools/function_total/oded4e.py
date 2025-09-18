def round_to_nearest(number: float, place: int) -> float:
    shift = 10 ** place
    return round(number * shift) / shift
