def sum_combinations(s: set) -> dict:
    sums = {}
    for x in s:
        for y in s:
            if x < y:
                pair_sum = x + y
                if pair_sum in sums:
                    sums[pair_sum] += 1
                else:
                    sums[pair_sum] = 1
    return sums
