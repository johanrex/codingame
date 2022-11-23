# Death First Search - Episode 1
# Problem description at: https://www.codingame.com/ide/puzzle/death-first-search-episode-1


from solution import Solution


def log(*objects):
    import sys

    print(*objects, file=sys.stderr, flush=True)


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

solution = Solution(n)

for i in range(l):
    # n1, n2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    solution.add_link(n1, n2)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    solution.add_exit_gateway(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    u, v = solution.cut(si)
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(u, v)
