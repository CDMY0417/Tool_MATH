def filter_positive_solution(numbers: tuple) -> float:
    for number in numbers:
        if number > 0:
            return number
    return None
