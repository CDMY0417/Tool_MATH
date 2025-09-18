def find_greatest_under_limit(limit: int, step: int, offset: int) -> int:
    quotient = (limit - offset) // step
    return step * quotient + offset
