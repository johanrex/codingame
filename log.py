def log(msg):
    import sys

    print(msg, file=sys.stderr, flush=True)
