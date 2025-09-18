def count_rectangles_with_lines(horizontal_lines: int, vertical_lines: int) -> int:
    return (horizontal_lines * (horizontal_lines - 1) // 2) * (vertical_lines * (vertical_lines - 1) // 2)
