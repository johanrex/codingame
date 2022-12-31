import sys


def log(*objects):
    print(*objects, file=sys.stderr, flush=True)

def logged_input():
    s = input()
    log("INPUT:", s)
    return s

import sys
import typing

class Graph:
    def __init__(self) -> None:
        self.nodes: list = []
        self.edges: dict[object, list] = {}

    def add_node(self, node):
        assert isinstance(node, typing.Hashable)
        assert node not in self.nodes

        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, u, v):
        assert v not in self.edges[u]
        assert u not in self.edges[v]

        self.edges[u].append(v)
        self.edges[v].append(u)

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        self.edges[v].remove(u)

    def bfs(self, src):
        visited = {}
        pred = {} #predecessors
        dist = {} #distance

        for node in self.nodes:
            dist[node] = sys.maxsize
            pred[node] = -1
            visited[node] = False

        visited[src] = True
        dist[src] = 0
        q = [src]

        while len(q) != 0:
            u = q.pop(0)
            for v in self.edges[u]:
                if visited[v] == False:
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    pred[v] = u
                    q.append(v)

        return dist, pred

class GraphUtils:
    @staticmethod
    def get_path(dest, pred) -> list[object]:
        path = []
        crawl = dest
        path.append(crawl)

        while pred[crawl] != -1:
            path.append(pred[crawl])
            crawl = pred[crawl]

        return path


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
# Death First Search - Episode 1
# Problem description at: https://www.codingame.com/ide/puzzle/death-first-search-episode-1




def main():
    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
    n, l, e = [int(i) for i in logged_input().split()]

    s = Solution(n)

    for _ in range(l):
        # n1, n2 defines a link between these nodes
        n1, n2 = [int(j) for j in logged_input().split()]
        s.add_link(n1, n2)

    for _ in range(e):
        ei = int(logged_input())  # the index of a gateway node
        s.add_exit_gateway(ei)

    # game loop
    while True:
        try:
            si = int(logged_input())  # The index of the node on which the Bobnet agent is positioned this turn
        except EOFError:
            break

        u, v = s.link_to_cut(si)
        s.remove_link(u,v)
        
        print(u, v, flush=True)

if __name__ == "__main__":
    main()
