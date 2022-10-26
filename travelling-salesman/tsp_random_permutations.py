import sys
import numpy as np
from scipy import spatial


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def read_input_from_stdin():
    inputs = []
    n = int(input())
    for i in range(n):
        coord = tuple((int(j) for j in input().split()))
        inputs.append(coord)

    return inputs


def calc_distance_random_permutations(inputs):
    def total_distance(a):
        prev = None
        total_distance = 0
        for curr in a:
            if prev is None:
                prev = curr
                continue
            else:
                total_distance += spatial.distance.euclidean(prev, curr)
        return total_distance

    memo = {}

    start = np.array([inputs[0]])
    rest = np.array(inputs[1:])

    samples = 2000
    min_d = sys.maxsize
    min_a = None

    for current_iteration in range(samples):
        a = np.concatenate((start, rest, start))
        bytes = a.tobytes()
        if bytes not in memo:
            memo[bytes] = None
            d = total_distance(a)
            if d < min_d:
                log(f"New min distance found: {d}")
                min_d = d
                min_a = a

        rest = np.random.permutation(rest)

    # translate to indexes
    indexes = []
    for node in min_a:
        node = tuple(node)
        indexes.append(str(inputs.index(node)))

    return min_d, indexes


if __name__ == "__main__":
    inputs = read_input_from_stdin()
    shortest_distance, indexes = calc_distance_random_permutations(inputs)
    print(" ".join(indexes))
