def days_until_balances_equal(principal1: float, rate1: float, principal2: float, rate2: float) -> int:
    return int((principal2 - principal1) / ((rate1 - rate2) * principal1))
