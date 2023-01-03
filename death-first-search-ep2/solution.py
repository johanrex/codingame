from collections import Counter
import itertools
from graph import Graph, GraphUtils


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

        #if we cut the last link to a node, remove all knowledge of it from state. 
        ns = [n1, n2]
        for n in ns:
            if len(self.g.edges[n]) == 0:
                self.g.remove_node(n)
                if n in self.exit_gateways:
                    self.exit_gateways.remove(n)

    def add_exit_gateway(self, e):
        self.exit_gateways.append(e)

    def link_to_cut(self, agent_id):
        g = self.g
        dist, pred = g.bfs(agent_id)

        # paths = []
        # for eg in self.exit_gateways:
        #     path = GraphUtils.get_path(eg, pred)
        #     paths.append(path)
        
        #is agent next to exit node?
        if (eg := next((eg for eg in self.exit_gateways if dist[eg] == 1), None)) is not None:
            u = agent_id
            v = eg
        else:
            #find nodes connected to more than one exit node, pick the most urgent one to cut.
            nodes_adjacent_exits = []
            for eg in self.exit_gateways:
                nodes_adjacent_exits.extend(g.edges[eg])

            c = Counter(nodes_adjacent_exits)
            #c_sorted = sorted(c, key=lambda x:c[x], reverse=True) #most common node first

            # calc urgency.
            node = c.most_common(1)[0][0]
            ns = g.edges[node]

            eg = next(n for n in ns if n in self.exit_gateways)
            u = eg
            v = node

        #paths.sort(key=lambda path: len(path))

        assert u is not None
        assert v is not None
        return u, v
