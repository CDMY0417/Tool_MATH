def square_less_than_threshold(values: list[int], threshold: int):
    return [x for x in values if x * x < threshold]
