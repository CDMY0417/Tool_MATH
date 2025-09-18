def dot_product(vector1: tuple, vector2: tuple) -> float:
    return sum(vector1[i] * vector2[i] for i in range(len(vector1)))
