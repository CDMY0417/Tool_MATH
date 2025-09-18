def weighted_combination(vector_a: list, vector_b: list, weight_a: float, weight_b: float) -> list:
    return [weight_a * ai + weight_b * bi for ai, bi in zip(vector_a, vector_b)]
