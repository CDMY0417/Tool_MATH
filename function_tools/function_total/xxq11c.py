def law_of_cosines_length(CB: float, CD: float, cos_angle_B: float) -> float:
    return (CB**2 + CD**2 - 2 * CB * CD * cos_angle_B) ** 0.5
