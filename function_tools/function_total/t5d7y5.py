def generate_pairs_congruent_to_mod(numbers: list[int], k: int, congruent_to: int):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if (numbers[i] + numbers[j]) % k == congruent_to:
                pairs.append((numbers[i], numbers[j]))
    return pairs
