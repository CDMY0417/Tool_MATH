def generate_pairs_add_up_to_multiple_of_k(numbers: list[int], k: int):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if (numbers[i] + numbers[j]) % k == 0:
                pairs.append((numbers[i], numbers[j]))
    return pairs
