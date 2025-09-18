def generate_all_pairs(s: set) -> list:
    return [(a, b) for a in s for b in s if a < b]
