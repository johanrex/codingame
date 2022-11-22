def log(*objects):
    import sys

    for obj in objects:
        print(obj, file=sys.stderr, end="", flush=True)
    print("")
