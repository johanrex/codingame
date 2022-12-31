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

    def add_exit_gateway(self, e):
        self.exit_gateways.append(e)

    def link_to_cut(self, agent_id):
        dist, pred = self.g.bfs(agent_id)

        path_infos = []
        for eg in self.exit_gateways:
            cost = dist[eg]
            path = GraphUtils.get_path(eg, pred)
            path_infos.append([cost, path])

        #for each common node, decrease the cost of the path by 1
        #we can't trust the cost of the path anymore, but relative cost is still valid
        for i in range(len(path_infos)):
            _, path = path_infos[i]
            for j in range(i+1, len(path_infos)):
                _, other_path = path_infos[j]

                for node in path:
                    if node != agent_id and node in other_path:
                        path_infos[i][0] -=1
                        path_infos[j][0] -=1

        #sort on the cost that we store in first pos in list. 
        path_infos.sort()

        path_to_exit_gateway_with_shortest_path = path_infos[0][1]
        u = path_to_exit_gateway_with_shortest_path[0]
        v = path_to_exit_gateway_with_shortest_path[1]

        # TODO, if no links to exit gateway anymore, remove it from graph.

        return u, v
