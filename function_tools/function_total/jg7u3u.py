def arrangements_with_fixed_distribution(distribution: tuple[int], num_bins: int) -> int:
    from math import factorial
    num_items = sum(distribution)
    distribution_count = len(distribution)
    if distribution_count > num_bins:
        return 0  # More groups than bins
    unique_bins = factorial(num_bins)
    for distinct_items in distribution:
        unique_bins //= factorial(distribution.count(distinct_items))
    return unique_bins
