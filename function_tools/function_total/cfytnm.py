def perfect_squares_in_range(lo: int, hi: int):
    squares = []
    i = int(lo**0.5)
    while i * i <= hi:
        if i * i >= lo:
            squares.append(i * i)
        i += 1
    return squares
