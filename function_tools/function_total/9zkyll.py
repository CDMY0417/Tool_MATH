import math
from typing import Tuple

def simplify_coefficients(coefficients: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
    gcd_value = math.gcd(math.gcd(coefficients[0], coefficients[1]), math.gcd(coefficients[2], coefficients[3]))
    simplified = tuple(c // gcd_value for c in coefficients)
    if simplified[0] < 0:
        simplified = tuple(-c for c in simplified)
    return simplified
