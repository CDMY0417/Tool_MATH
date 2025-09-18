def reflect_point_across_plane(point: tuple, plane_point: tuple, normal_vector: tuple):
    px, py, pz = point
    nx, ny, nz = normal_vector
    d = -(nx * plane_point[0] + ny * plane_point[1] + nz * plane_point[2])
    t = -((nx * px + ny * py + nz * pz + d) / (nx * nx + ny * ny + nz * nz)) * 2
    reflected_point = (px + t * nx, py + t * ny, pz + t * nz)
    return reflected_point
