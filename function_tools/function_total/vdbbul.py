def is_palindrome(number: int) -> bool:
    s = str(number)
    return s == s[::-1]
