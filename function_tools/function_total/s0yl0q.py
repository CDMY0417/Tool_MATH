def calculate_group_mean_age(ages_counts: dict[int, int]) -> float:
    total_age = sum(age * count for age, count in ages_counts.items())
    total_people = sum(ages_counts.values())
    return total_age / total_people
