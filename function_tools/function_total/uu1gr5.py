def cosine_similarity(v1: tuple, v2: tuple):
    num = sum(i * j for i, j in zip(v1, v2))
    den = (sum(i**2 for i in v1) ** 0.5) * (sum(j**2 for j in v2) ** 0.5)
    return num / den
