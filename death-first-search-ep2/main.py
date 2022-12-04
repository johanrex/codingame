# Death First Search - Episode 1
# Problem description at: https://www.codingame.com/ide/puzzle/death-first-search-episode-1


from solution import Solution
from log import log, logged_input


def main():
    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
    n, l, e = [int(i) for i in logged_input().split()]

    solution = Solution(n)

    for _ in range(l):
        # n1, n2 defines a link between these nodes
        n1, n2 = [int(j) for j in logged_input().split()]
        solution.add_link(n1, n2)

    for _ in range(e):
        ei = int(logged_input())  # the index of a gateway node
        solution.add_exit_gateway(ei)

    # game loop
    while True:
        try:
            si = int(logged_input())  # The index of the node on which the Bobnet agent is positioned this turn
        except EOFError:
            break

        u, v = solution.cut(si)

        # Example: 0 1 are the indices of the nodes you wish to sever the link between
        print(u, v, flush=True)


if __name__ == "__main__":
    main()
