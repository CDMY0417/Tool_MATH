def is_divisible_by_all_except_two(n: int, start: int, end: int, exclude_start: int) -> bool:
    for i in range(start, end + 1):
        if i != exclude_start and i != exclude_start + 1:
            if n % i != 0:
                return False
    return True
