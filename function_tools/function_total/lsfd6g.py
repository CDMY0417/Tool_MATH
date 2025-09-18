def sum_repeated_pattern(pattern: list[int], times: int) -> int:
    full_cycles = times // len(pattern)
    remainder = times % len(pattern)
    return full_cycles * sum(pattern) + sum(pattern[:remainder])
