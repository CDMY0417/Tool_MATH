def substitute_and_evaluate_fraction(numerator_expr: tuple[tuple[float, str], ...], denominator_expr: tuple[tuple[float, str], ...], substitutions: dict[str, float]) -> float:
    numerator_value = sum(coef * substitutions[var] for coef, var in numerator_expr)
    denominator_value = 1
    for coef, var in denominator_expr:
        denominator_value *= coef * substitutions[var]
    return numerator_value / denominator_value
