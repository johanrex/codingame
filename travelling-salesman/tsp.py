# Problem description:
# https://www.codingame.com/ide/puzzle/travelling-salesman

from functools import cache
from itertools import permutations
import sys
import math


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


if __name__ == "__main__":
    inputs = read_input_from_stdin()
    route = calc_distance_brute_force(inputs)
    print(route)
