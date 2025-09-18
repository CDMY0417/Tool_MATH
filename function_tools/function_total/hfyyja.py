def is_palindrome(number: int) -> bool:
    number_str = str(number)
    return number_str == number_str[::-1]
