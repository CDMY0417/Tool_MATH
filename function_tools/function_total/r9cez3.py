def is_within_circle(x: float, y: float, h: float, k: float, r: float) -> bool:
    return (x - h) ** 2 + (y - k) ** 2 < r ** 2
