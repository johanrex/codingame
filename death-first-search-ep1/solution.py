from graph import Graph


class Solution:
    def __init__(self, n) -> None:
        self.n: int

        self.g = Graph()
        for i in range(n):
            self.g.add_node(i)

        self.exit_gateways = []

    def add_link(self, n1, n2):
        self.g.add_edge(n1, n2)

    def add_exit_gateway(self, e):
        self.exit_gateways.append(e)

    def cut(self, agent_idx):
        all_paths = []
        for eg in self.exit_gateways:
            all_paths.extend(self.g.get_paths(agent_idx, eg))

        tmp = all_paths[0]
        u, v = tmp[0], tmp[1]
        return u, v
