import sys
from log import log


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

    # from: https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
    def bfs(self, src):

        nr_of_nodes = len(self.nodes)

        # predecessor[i] array stores predecessor of
        # i and distance array stores distance of i
        # from s
        pred = [0 for _ in range(nr_of_nodes)]
        dist = [0 for _ in range(nr_of_nodes)]

        # a queue to maintain queue of vertices whose
        # adjacency list is to be scanned as per normal
        # DFS algorithm
        queue = []

        # boolean array visited[] which stores the
        # information whether ith vertex is reached
        # at least once in the Breadth first search
        visited = [False for _ in range(nr_of_nodes)]

        # initially all vertices are unvisited
        # so v[i] for all i is false
        # and as no path is yet constructed
        # dist[i] for all i set to infinity
        for i in range(nr_of_nodes):

            dist[i] = sys.maxsize
            pred[i] = -1

        # now source is first to be visited and
        # distance from source to itself should be 0
        visited[src] = True
        dist[src] = 0
        queue.append(src)

        # standard BFS algorithm
        while len(queue) != 0:
            u = queue[0]
            queue.pop(0)

            for i in range(len(self.edges[u])):

                if visited[self.edges[u][i]] == False:
                    visited[self.edges[u][i]] = True
                    dist[self.edges[u][i]] = dist[u] + 1
                    pred[self.edges[u][i]] = u
                    queue.append(self.edges[u][i])

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
