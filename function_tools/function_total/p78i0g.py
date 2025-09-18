def find_parabola_focus(a: float, h: float, k: float):
    focus_y = k + 1 / (4 * a)
    return (h, focus_y)
