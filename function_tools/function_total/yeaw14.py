def domain_of_rational_function(excluded: set) -> list:
    intervals = []
    previous = -float('inf')
    excluded = sorted(excluded)
    for e in excluded:
        intervals.append((previous, e))
        previous = e
    intervals.append((previous, float('inf')))
    return intervals
