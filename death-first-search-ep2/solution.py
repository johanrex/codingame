from collections import Counter
import itertools
from graph import Graph, GraphUtils
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
        dist, pred = self.g.bfs(agent_id)

        paths = []
        for eg in self.exit_gateways:
            path = GraphUtils.get_path(eg, pred)
            paths.append(path)

        paths.sort(key=lambda path: len(path))

        shortest_path = len(paths[0])
        shortest_paths = [path for path in paths if len(path) == shortest_path]

        #is there only one shortest path? 
        if len(shortest_paths) == 1: 
            path = shortest_paths[0]
        else: 
            #no, we have more than one path with shortest length
            #choose the one with most common nodes
            nodes = itertools.chain(*shortest_paths)
            c = Counter(nodes)
            del c[agent_id]
            #get most common node
            most_common_node = c.most_common(1)[0][0]

            #choose paths containing the most common node
            shortest_paths_containing_most_common_node = [path for path in shortest_paths if most_common_node in path]
            
            #pick one random, they should be equivalent. 
            path = shortest_paths_containing_most_common_node[0]

        u = path[0]
        v = path[1]

        return u, v
