def sum_of_numbers_excluding(start: int, end: int, exclude: set):
    return sum(i for i in range(start, end + 1) if i not in exclude)
