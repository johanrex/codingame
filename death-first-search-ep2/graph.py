import sys
from log import log
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

    def remove_node(self, node):
        assert isinstance(node, typing.Hashable)
        assert node in self.nodes

        del self.edges[node]
        self.nodes.remove(node)

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
