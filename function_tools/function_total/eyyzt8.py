def nested_functions(a1: int, b1: int, a2: int, b2: int, x: int) -> int:
    inner_result = a1 * x + b1
    return a2 * inner_result + b2
