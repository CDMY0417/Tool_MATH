def count_specific_items(items: dict[str, int], keys: set[str]) -> int:
    return sum(items[key] for key in keys if key in items)
