def scale_ratio(ratio_base: int, ratio_height: int, desired_base: int) -> float:
    factor = desired_base / ratio_base
    return ratio_height * factor
