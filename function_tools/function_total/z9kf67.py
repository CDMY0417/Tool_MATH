def transform_and_scale_sequence(sequence: list[int], add_constant: int, scale_divisor: int) -> list[int]:
    return [(x + add_constant) // scale_divisor for x in sequence]
