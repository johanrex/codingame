import sys
import math


def log(msg):
    print(msg, file=sys.stderr, flush=True)


class CostCache:
    def __init__(self, inputs) -> None:
        self.inputs = inputs
        self.cost = None
        self.tpl_to_idx = {}

        self.__cost_lookup_init(inputs)

    def __cost_lookup_init(self, inputs):
        length = len(self.inputs)
        self.costs = [[None for i in range(length)] for j in range(length)]  # Init empty 2D array.

        for x in range(length):
            n1 = self.inputs[x]

            # Init tpl to idx cache
            self.tpl_to_idx[n1] = x

            # Calc cost matrix
            for y in range(length):
                n2 = self.inputs[y]
                if n1 == n2:
                    cost = 0
                else:
                    cost = CostCache.__calc_cost(n1, n2)

                log(f"{n1} -> {n2} cost: {cost}. Putting at place x:{x} y:{y}.")

                self.costs[x][y] = cost

    @staticmethod
    def __calc_cost(n1, n2):
        x1, y1 = n1
        x2, y2 = n2
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return dist

    def cost_lookup(self, n1, n2):
        x = self.tpl_to_idx[n1]
        y = self.tpl_to_idx[n2]
        cost = self.costs[x][y]

        return cost

    def route_cost(self, route):
        total_cost = 0
        first = True
        prev = None
        for curr in route:
            if first:
                first = False
                prev = curr
            else:
                total_cost += self.cost_lookup(prev, curr)

        return total_cost


def two_opt_swap(route, i, j):
    new_route = []

    # 1. take route[0] to route[v1] and add them in order to new_route
    new_route.append(route[0 : i + 1])

    # 2. take route[v1+1] to route[v2] and add them in reverse order to new_route
    new_route.append(route[i + 1 : j + 1].reverse())

    # 3. take route[v2+1] to route[end] and add them in order to new_route
    new_route.append(route[j + 1 :])

    return new_route


inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]

cost_cache = CostCache(inputs)

# Add path back to start.
existing_route = [*inputs, inputs[0]]

best_cost = cost_cache.route_cost(existing_route)
nr_of_nodes_to_swap = len(existing_route) - 1  # Don't swap first and last node in route.
improvement = True
while improvement:
    improvement = False
    for i in range(1, nr_of_nodes_to_swap):
        for j in range(i, nr_of_nodes_to_swap):
            new_route = two_opt_swap(existing_route, i, j)
            new_cost = cost_cache.route_cost(new_route)  # TODO optimize
            if new_cost < best_cost:
                existing_route = new_route
                best_cost = new_cost
                improvement = True


# TODO random ordering of the nodes at start
