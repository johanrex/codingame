def log(*objects):
    import sys
    print(*objects, file=sys.stderr, flush=True)
