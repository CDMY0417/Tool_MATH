def herons_formula_area_squared(semi_perimeter: float, side_a: float, side_b: float, side_c: float) -> float:
    return semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)
