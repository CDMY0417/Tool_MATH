def calculate_median(numbers: list[float]) -> float:
    n = len(numbers)
    sorted_numbers = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
