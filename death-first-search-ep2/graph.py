import sys
import typing
import copy

class Graph:
    def __init__(self) -> None:
        self.nodes: list = []
        self.edges: dict[object, list] = {}

    def copy(self):
        new_graph = Graph()
        new_graph.nodes = copy.deepcopy(self.nodes)
        new_graph.edges = copy.deepcopy(self.edges)
        return new_graph

    def add_node(self, node):
        assert isinstance(node, typing.Hashable)
        assert node not in self.nodes

        self.nodes.append(node)
        self.edges[node] = []

    def remove_node(self, node):
        assert isinstance(node, typing.Hashable)
        assert node in self.nodes

        #remove from neighbors
        for e in self.edges[node]:
            self.edges[e].remove(node)

        del self.edges[node]
        self.nodes.remove(node)

        #TODO it's possible that this leaves an orphaned node if the node we removed was the only link to it. 


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
