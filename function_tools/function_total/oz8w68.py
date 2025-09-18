def probability_same_color(green_balls: int, red_balls: int) -> float:
    total_balls = green_balls + red_balls
    prob_two_greens = (green_balls / total_balls) ** 2
    prob_two_reds = (red_balls / total_balls) ** 2
    return prob_two_greens + prob_two_reds
