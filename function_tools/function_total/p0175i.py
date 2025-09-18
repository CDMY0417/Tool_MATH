def average_of_numbers(numbers: list[float]) -> float:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
