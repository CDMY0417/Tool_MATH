def total_edge_length_of_pyramid(side_length: float, slant_edge_length: float) -> float:
    base_perimeter = 4 * side_length
    apex_edges_length = 4 * slant_edge_length
    return base_perimeter + apex_edges_length
