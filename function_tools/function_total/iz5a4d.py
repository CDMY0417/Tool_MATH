def convert_currency(amount: float, exchange_rate: float) -> float:
    return round(amount / exchange_rate, 2)
