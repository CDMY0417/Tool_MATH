def intersection_of_line_and_plane(line_point: tuple, direction_vector: tuple, normal_vector: tuple, plane_point: tuple):
    a, b, c = normal_vector
    x0, y0, z0 = line_point
    d = -(a * plane_point[0] + b * plane_point[1] + c * plane_point[2])
    x_dir, y_dir, z_dir = direction_vector
    t_numerator = -(a * x0 + b * y0 + c * z0 + d)
    t_denominator = (a * x_dir + b * y_dir + c * z_dir)
    t = t_numerator / t_denominator
    intersection_point = (x0 + t * x_dir, y0 + t * y_dir, z0 + t * z_dir)
    return intersection_point
