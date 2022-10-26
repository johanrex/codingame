# Problem description:
# https://www.codingame.com/ide/puzzle/travelling-salesman

from functools import cache
from itertools import permutations
import sys
import math
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


@cache
def get_distance(n1, n2):
    x1, y1 = n1
    x2, y2 = n2

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def calc_distance_nearest_neighbor(inputs):
    current = inputs[0]
    nodes_to_visit = inputs[1:]
    route = []
    route.append(current)
    while len(nodes_to_visit) > 0:
        x1, y1 = current
        distances = []
        for node in nodes_to_visit:
            x2, y2 = node

            dist = get_distance(current, node)
            distances.append([dist, node])

        distances.sort()
        closest_dist, closest_node = distances[0]
        nodes_to_visit.remove(closest_node)
        route.append(closest_node)
        current = closest_node

    route.append(route[0])

    indexes = []
    # translate to indexes
    for node in route:
        indexes.append(str(inputs.index(node)))

    return " ".join(indexes)


def calc_distance_brute_force(inputs):
    all_distances_and_routes = []
    start = inputs[0]
    nodes_to_visit = inputs[1:]

    ps = permutations(nodes_to_visit)
    for p in ps:
        current_route = [start, *p, start]
        total_distance = 0

        prev = None
        for node in current_route:
            if prev is None:
                prev = node
                continue
            else:
                d = get_distance(prev, node)
                total_distance += d
                prev = node

        all_distances_and_routes.append([total_distance, current_route])

    all_distances_and_routes.sort()
    shortest_distance_route = all_distances_and_routes[0]
    shortest_route = shortest_distance_route[1]

    indexes = []
    # translate to indexes
    for node in shortest_route:
        indexes.append(str(inputs.index(node)))

    return " ".join(indexes)


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

    indexes = []
    # translate to indexes
    for node in min_a:
        node = tuple(node)
        indexes.append(str(inputs.index(node)))

    return " ".join(indexes)


if __name__ == "__main__":
    inputs = read_input_from_stdin()
    # route = calc_distance_brute_force(inputs)
    route = calc_distance_random_permutations(inputs)
    print(route)
