def equivalent_arrangement_groups(arrangements_count: int, rotations: int, reflections: int) -> int:
    return arrangements_count // (rotations * reflections)
