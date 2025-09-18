def is_palindrome(num: int) -> bool:
    s = str(num)
    return s == s[::-1]
