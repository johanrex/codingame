import sys


def log(*objects, log_func=print):
    log_func(*objects, file=sys.stderr, flush=True)

def logged_input(_input=input):
    s = _input()
    log("INPUT:", s)
    return s

