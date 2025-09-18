def day_of_week_on_the_nth_day(first_day_of_week: int, n: int) -> int:
    remainder = n % 7
    return (first_day_of_week + remainder - 1) % 7
