import sys

# perf_counter = 0

# Directed graph
class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        # TODO make sure it's hashable
        # TODO make sure it's not already added
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, u, v):
        # TODO make sure it's not already added.
        self.edges[u].append(v)
        self.edges[v].append(u)

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        self.edges[v].remove(u)

    def __get_shortest_path(self, shortest_path, current_path, u, vs):
        # global perf_counter
        # perf_counter += 1

        current_path = current_path + [u]
        if u in vs:
            if len(shortest_path) == 0:
                shortest_path.extend(current_path)
            else:
                if len(current_path) < len(shortest_path):
                    shortest_path.clear()
                    shortest_path.extend(current_path)
        else:
            if len(shortest_path) == 0 or len(current_path) < len(shortest_path):
                for e in self.edges[u]:
                    if e not in current_path:
                        self.__get_shortest_path(shortest_path, current_path, e, vs)

    def get_shortest_path(self, u, v) -> list[object]:
        # TODO check if u, v is in graph
        assert u != v

        shortest_path = []  # all paths leading from u to v
        current_path = []
        self.__get_shortest_path(shortest_path, current_path, u, v)
        return shortest_path
