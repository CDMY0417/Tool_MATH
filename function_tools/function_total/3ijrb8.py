def calculate_total_items(group_counts: list[int], items_per_group: list[int]) -> int:
    return sum(count * items for count, items in zip(group_counts, items_per_group))
