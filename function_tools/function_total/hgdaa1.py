def pythagorean_theorem(a: float, b: float, hypotenuse: bool) -> float:
    if hypotenuse:
        return (a**2 + b**2)**0.5
    else:
        return (b**2 - a**2)**0.5
