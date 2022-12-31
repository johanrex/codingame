import sys
from log import log
import typing

# Directed graph
class Graph:
    def __init__(self) -> None:
        self.nodes: list = []
        self.edges: dict = {}

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
        nr_of_nodes = len(self.nodes)

        visited = [False] * nr_of_nodes
        pred = [0] * nr_of_nodes
        dist = [0] * nr_of_nodes

        for i in range(nr_of_nodes):
            dist[i] = sys.maxsize
            pred[i] = -1

        visited[src] = True
        dist[src] = 0

        q = []
        q.append(src)

        while len(q) != 0:
            u = q.pop(0)
            for i in range(len(self.edges[u])):
                if visited[self.edges[u][i]] == False:
                    visited[self.edges[u][i]] = True
                    dist[self.edges[u][i]] = dist[u] + 1
                    pred[self.edges[u][i]] = u
                    q.append(self.edges[u][i])

        return dist, pred

    def get_path(self, dest, pred) -> list[object]:
        # vector path stores the shortest path
        path = []
        crawl = dest
        path.append(crawl)

        while pred[crawl] != -1:
            path.append(pred[crawl])
            crawl = pred[crawl]

        return path
