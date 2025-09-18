def vector_detection(vector: tuple) -> bool:
    return all(component == 0 for component in vector)
