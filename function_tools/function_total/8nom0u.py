from math import comb

def ball_and_urn_ways(balls: int, urns: int) -> int:
    return comb(balls + urns - 1, urns - 1)
