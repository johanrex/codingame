import collections
from typing import Self
from enum import Enum


# agent, gateway.


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

    def __get_paths(self, paths, path, u, v):
        path = path + [u]
        if u == v:
            paths.append(path)
        else:
            for e in self.edges[u]:
                if e not in path:
                    self.__get_paths(paths, path, e, v)

    def get_paths(self, u, v) -> list[object]:
        # TODO check if u, v is in graph
        assert u != v

        paths = []  # all paths leading from u to v
        path = []
        self.__get_paths(paths, path, u, v)
        return paths


class GraphNode:
    def __init__(self, id) -> None:
        self.id = id
        self.tags = {}
        self.edges = []

    def add_edge(self, node: Self):
        self.edges.append(node)
