def calculate_mode(numbers: list[int]) -> int:
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return min(modes)
