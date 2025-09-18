def cents_to_dollars(cents: int) -> str:
    dollars = cents // 100
    leftover_cents = cents % 100
    return f'${dollars}.{leftover_cents:02d}'
