def angle_bisector_theorem_segment(AB: int, AC: int, BC: int) -> float:
    ratio = AB / AC
    DC = (BC * ratio) / (1 + ratio)
    return DC
