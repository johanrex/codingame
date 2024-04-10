# Problem:
# https://www.codingame.com/ide/puzzle/six-degrees-of-kevin-bacon

import sys
from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    value: str
    neighbors: set[str]


def log(*objects):
    # debug-logging in codingame is defined like this.
    print(*objects, file=sys.stderr, flush=True)


def parse_movie_line(line):
    tmp = line.split(":")
    title = tmp[0]
    actors = tmp[1].split(",")
    actors = [actor.strip() for actor in actors]
    return title, set(actors)


def parse_input() -> tuple[str, dict[str, set[str]]]:
    movies: dict[str, set[str]] = dict()

    source_actor = input()
    n = int(input())
    for _ in range(n):
        movie_cast = input()
        title, actors = parse_movie_line(movie_cast)
        movies[title] = actors

    return source_actor, movies


def build_graph(movies) -> dict[str, Node]:
    g: dict[str, Node] = dict()
    for title in movies:
        actors = movies[title]

        for actor in actors:
            neighbors = actors.copy()
            neighbors.remove(actor)

            if actor in g:
                node = g[actor]
                node.neighbors |= neighbors
            else:
                node = Node(value=actor, neighbors=neighbors)
                g[actor] = node
    return g


def dfs(g: dict[str, Node], actor, curr_path, shortest_path=sys.maxsize):
    curr_path.append(actor)

    if len(curr_path) < shortest_path:
        if actor == "Kevin Bacon":
            if len(curr_path) < shortest_path:
                log(
                    f"Found new shortest path with length {len(curr_path)}: {curr_path}"
                )

                shortest_path = len(curr_path)
            return shortest_path

        node = g[actor]
        for neighbor in node.neighbors:
            if neighbor not in curr_path:
                tmp = dfs(g, neighbor, [*curr_path], shortest_path)
                shortest_path = min(shortest_path, tmp)

    return shortest_path


def bfs(g: dict[str, Node], source_actor: str) -> int:
    shortest_path = sys.maxsize

    visited = {source_actor}
    q = deque([(source_actor, 1)])

    while len(q) > 0:
        actor, distance = q.popleft()

        # prune long paths
        if distance > shortest_path:
            continue

        if actor == "Kevin Bacon":
            shortest_path = distance

        for neighbor in g[actor].neighbors:
            if neighbor not in visited:
                q.append((neighbor, distance + 1))

    return shortest_path


def get_bacon_nr(source_actor: str, g: dict[str, Node]):
    # shortest_path = dfs(g, source_actor, [])
    shortest_path = bfs(g, source_actor)

    bacon_nr = shortest_path - 1
    return bacon_nr


if __name__ == "__main__":
    source_actor, movies = parse_input()

    log(source_actor)
    for movie in movies:
        log(f"'{movie}': {movies[movie]},")

    g = build_graph(movies)

    bacon_nr = get_bacon_nr(source_actor, g)

    print(bacon_nr)
