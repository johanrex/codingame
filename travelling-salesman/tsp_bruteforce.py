from functools import cache
from itertools import permutations
import math
import sys


def log(msg):
    print(msg, file=sys.stderr, flush=True)


@cache
def get_distance(n1, n2):
    x1, y1 = n1
    x2, y2 = n2

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def read_input_from_stdin():
    inputs = []
    n = int(input())
    for i in range(n):
        coord = tuple((int(j) for j in input().split()))
        inputs.append(coord)

    return inputs


def route_cost(route):
    total_cost = 0
    first = True
    prev = None
    for curr in route:
        if first:
            first = False
        else:
            total_cost += get_distance(prev, curr)
        prev = curr

    return total_cost


def calc_distance_brute_force(inputs):
    all_distances_and_routes = []
    start = inputs[0]
    nodes_to_visit = inputs[1:]

    ps = permutations(nodes_to_visit)
    for p in ps:
        current_route = [start, *p, start]
        total_distance = route_cost(current_route)

        all_distances_and_routes.append([total_distance, current_route])

    all_distances_and_routes.sort()
    shortest_distance_route = all_distances_and_routes[0]
    shortest_distance = shortest_distance_route[0]
    shortest_route = shortest_distance_route[1]

    indexes = []
    # translate to indexes
    for node in shortest_route:
        indexes.append(str(inputs.index(node)))

    return shortest_distance, indexes


if __name__ == "__main__":
    inputs = read_input_from_stdin()
    shortest_distance, indexes = calc_distance_brute_force(inputs)
    print(" ".join(indexes))
