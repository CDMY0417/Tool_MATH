def divisibility_check_for_7(number: int) -> bool:
    while number > 0:
        if number < 7:
            return False
        next_number = number // 10 - 2 * (number % 10)
        if next_number == 0:
            return True
        number = abs(next_number)
    return False
