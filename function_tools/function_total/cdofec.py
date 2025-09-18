def units_digit_property(number: int) -> bool:
    return (number * number) % 10 == number % 10
