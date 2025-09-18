def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]
