def leftmost_digits(n: int, count: int) -> int:
    digits = str(n)
    result = ''
    for char in digits:
        if char != '0':
            result += char
            if len(result) == count:
                break
    return int(result)
