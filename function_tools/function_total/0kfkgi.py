def num_integers_congruent_mod(start: int, end: int, target: int, mod_value: int) -> int:
    count = 0
    for num in range(start, end + 1):
        if num % mod_value == target:
            count += 1
    return count
