import sys
import math


def log(*objects):
    import sys

    for obj in objects:
        print(obj, file=sys.stderr, end="", flush=True)
    print("", file=sys.stderr, flush=True)


import sys
import math


def write(l, h, t, lines):
    # ord("A") -> 65
    # chr(65) -> "A"

    log(t)
    t = t.upper()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

    poss: list = []
    for c in t:
        pos = alphabet.find(c)
        if pos == -1:
            pos = len(alphabet)-1
        poss.append(pos)

    for line in lines:
        output_line = ""
        for pos in poss:
            output_line += line[pos * l : (pos * l) + l]

        print(output_line)


def main():
    l = int(input())
    h = int(input())
    t = input()

    lines = []

    for i in range(h):
        line = input()
        log(line)
        lines.append(line)

    write(l, h, t, lines)


def test():
    l = 4
    h = 5
    t = "M@NH@TT@N"
    lines = []
    lines.append(" #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ")
    lines.append("# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ")
    lines.append("### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ")
    lines.append("# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ")
    lines.append("# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ")

    write(l, h, t, lines)


if __name__ == "__main__":
    test()
    # main()
