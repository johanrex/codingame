# Death First Search - Episode 2
# Problem description at: https://www.codingame.com/ide/puzzle/death-first-search-episode-2

from solution import Solution
from log import logged_input

def main(input__=input, print_=print):
    input_ = lambda: logged_input(input__)

    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
    n, l, e = [int(i) for i in input_().split()]

    s = Solution(n)

    for _ in range(l):
        # n1, n2 defines a link between these nodes
        n1, n2 = [int(j) for j in input_().split()]
        s.add_link(n1, n2)

    for _ in range(e):
        ei = int(input_())  # the index of a gateway node
        s.add_exit_gateway(ei)

    # game loop
    while True:
        try:
            si = int(input_())  # The index of the node on which the Bobnet agent is positioned this turn
        except EOFError:
            break

        u, v = s.link_to_cut(si)
        s.remove_link(u,v)
        
        print_(u, v, flush=True)

if __name__ == "__main__":
    main()
