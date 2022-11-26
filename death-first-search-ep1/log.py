import sys


def log(*objects):
    print(*objects, file=sys.stderr, flush=True)

def logged_input():
    s = input()
    log("INPUT:", s)
    return s

