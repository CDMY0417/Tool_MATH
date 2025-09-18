def find_removable_number(numbers_set: set[int]) -> int:
    for number in numbers_set:
        if any(other != number and number % other == 0 for other in numbers_set):
            return number
    return None
