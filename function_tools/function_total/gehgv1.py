def calculate_segment_length(total_length: float, ratio_numerator: float, ratio_denominator: float) -> float:
    return total_length * ratio_numerator / (ratio_numerator + ratio_denominator)
