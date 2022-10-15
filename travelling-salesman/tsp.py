# Problem description:
# https://www.codingame.com/ide/puzzle/travelling-salesman

from functools import cache
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


if __name__ == "__main__":
    inputs = read_input_from_stdin()
    route = calc_distance_nearest_neighbor(inputs)
    print(route)
