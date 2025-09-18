def pascal_rule_combination(n: int, k: int, known: dict):
    if (n, k) in known:
        return known[(n, k)]
    if (n-1, k) in known and (n-1, k-1) in known:
        return known[(n-1, k)] + known[(n-1, k-1)]
    return None
