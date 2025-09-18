def cross_product(vector_a: tuple, vector_b: tuple):
    ax, ay, az = vector_a
    bx, by, bz = vector_b
    return (ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx)
