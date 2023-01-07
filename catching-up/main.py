import sys

import sys
import typing
import copy
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __cmp__(self, other) -> int:
        if self.x == other.x and self.y == other.y:
            return 0
        elif self.x < other.x:
            return -1
        elif self.x == other.x and self.y < other.y:
            return -1
        else:
            return 1

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __lt__(self, other):
        return self.__cmp__(other) == -1

    def __gt__(self, other):
        return self.__cmp__(other) == 1

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __hash__(self):
        return (self.x << 32) + self.y


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

        # remove from neighbors
        for e in self.edges[node]:
            self.edges[e].remove(node)

        del self.edges[node]
        self.nodes.remove(node)

        # TODO it's possible that this leaves an orphaned node if the node we removed was the only link to it.

    def add_edge(self, u, v):
        assert v not in self.edges[u]
        assert u not in self.edges[v]

        self.edges[u].append(v)
        self.edges[v].append(u)

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        self.edges[v].remove(u)

    def bfs(self, src, randomize=False):
        visited = {}
        pred = {}  # predecessors
        dist = {}  # distance

        for node in self.nodes:
            dist[node] = sys.maxsize
            pred[node] = None
            visited[node] = False

        visited[src] = True
        dist[src] = 0
        q = [src]

        while len(q) != 0:
            u = q.pop(0)

            edges = self.edges[u]

            #let's randomize the edges so we can get different paths
            random.shuffle(edges)

            for v in edges:
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

        while pred[crawl] is not None:
            path.append(pred[crawl])
            crawl = pred[crawl]

        return path


def log(*objects):
    # debug-logging in codingame is defined like this.
    print(*objects, file=sys.stderr, flush=True)


def logged_input():
    s = input()
    log("INPUT:", s)
    return s


def maybe_add_edge(g, u, v):
    if u in g.edges and v in g.edges and v not in g.edges[u]:
        g.add_edge(u, v)

g = Graph()
rows = 10
cols = 10

dir_up = Point(0, -1)
dir_down = Point(0, 1)
dir_left = Point(-1, 0)
dir_right = Point(1, 0)

k = int(logged_input())  # representing after how many turns the sus man will make another move

p = Point(-1, -1)
e = Point(-1, -1)

# create graph nodes
for y in range(rows):
    s = logged_input()  # the map
    for x in range(cols):

        # assuming the room has a border of *'s
        # if (y == 0 or y == (rows - 1)) and s[x] != "*":
        #     raise ValueError("adjust your assumptions about the room")

        # if (x == 0 or x == (rows - 1)) and s[x] != "*":
        #     raise ValueError("unexpected input")

        if s[x] != "*":
            curr = Point(x, y)
            g.add_node(curr)

            if s[x] == "E":
                e = curr
            elif s[x] == "P":
                p = curr

# Create the edges
for y in range(10):
    for x in range(10):
        curr = Point(x, y)
        if curr in g.edges:
            assert g.edges[curr] is not None

            maybe_add_edge(g, curr, curr + dir_up)
            maybe_add_edge(g, curr, curr + dir_down)
            maybe_add_edge(g, curr, curr + dir_left)
            maybe_add_edge(g, curr, curr + dir_right)


# game loop
while True:
    # ene_y: the sus man's coordinate,two integers separated by space in a single line
    # ene_x: the sus man's coordinate,two integers separated by space in a single line
    ene_y, ene_x = [int(i) for i in logged_input().split()]

    e = Point(ene_x, ene_y)
    dist, pred = g.bfs(p)
    path = GraphUtils.get_path(e, pred)
    path = list(reversed(path))

    curr = path[0]
    nxt = path[1]

    assert isinstance(curr, Point)
    assert isinstance(nxt, Point)

    tmp = nxt - curr

    #log("tmp:", tmp)
    if tmp == dir_up:
        print("U")
    elif tmp == dir_down:
        print("D")
    elif tmp == dir_left:
        print("L")
    elif tmp == dir_right:
        print("R")
    else:
        raise ValueError("unexpected direction")

    p = nxt