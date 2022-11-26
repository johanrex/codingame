from graph import Graph
from log import log


class Solution:
    def __init__(self, n) -> None:
        self.n: int

        self.g = Graph()
        for i in range(n):
            self.g.add_node(i)

        self.exit_gateways = []

    def add_link(self, n1, n2):
        self.g.add_edge(n1, n2)

    def remove_link(self, n1, n2):
        self.g.remove_edge(n1, n2)

    def add_exit_gateway(self, e):
        self.exit_gateways.append(e)

    def cut(self, agent_idx):

        shortest_path  = self.g.get_shortest_path(agent_idx, self.exit_gateways)

        u, v = shortest_path[0], shortest_path[1]

        self.g.remove_edge(u, v)

        return u, v
