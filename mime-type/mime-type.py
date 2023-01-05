import sys
from collections import defaultdict


def log(*objects):
    # debug-logging in codingame is defined like this.
    print(*objects, file=sys.stderr, flush=True)


def logged_input():
    s = input()
    log("INPUT:", s)
    return s


def file_extension(filename):
    if "." not in filename:
        return None
    return filename.split(".")[-1]


mt_lookup = defaultdict(lambda: "UNKNOWN") 

n = int(logged_input())  # Number of elements which make up the association table.
q = int(logged_input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = logged_input().split()
    mt_lookup[ext.lower()] = mt

filenames = []

for i in range(q):
    filenames.append(logged_input())  # One file name per line.

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
for filename in filenames:
    ext = file_extension(filename)
    print(mt_lookup[ext if ext is None else ext.lower()])
