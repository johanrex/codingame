from functools import cache
import sys
import math

# Problem description:
# https://www.codingame.com/ide/puzzle/the-travelling-salesman-problem


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


def calc_distance(inputs):
    current = inputs[0]
    nodes_to_visit = inputs[1:]
    total_distance = 0

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
        total_distance += closest_dist
        nodes_to_visit.remove(closest_node)
        route.append(closest_node)
        current = closest_node

    # add distance back to start
    dist = get_distance(current, route[0])
    total_distance += dist

    # TODO: If there are points with the same distance, always pick the one occurring first in the list.
    return round(total_distance)


if __name__ == "__main__":
    inputs = read_input_from_stdin()
    total_distance = calc_distance(inputs)
    print(total_distance)
