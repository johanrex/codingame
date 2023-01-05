import sys
import math


def log(*objects):
    # debug-logging in codingame is defined like this.
    print(*objects, file=sys.stderr, flush=True)


def logged_input():
    s = input()
    log("INPUT:", s)
    return s

def dist(lon_a, lat_a, lon_b, lat_b):
    x = (lon_b - lon_a) * math.cos((lat_a + lat_b) / 2)
    y = (lat_b - lat_a)
    return math.sqrt(x * x + y * y) * 6371

def parse_float(s)->float:
    return float(s.replace(',', '.'))

lon = parse_float(logged_input())
lat = parse_float(logged_input())
n = int(logged_input())

dists = {}

for i in range(n):
    fib = logged_input()
    tokens = fib.split(';')
    name = tokens[1]

    curr_lon = parse_float(tokens[4])
    curr_lat = parse_float(tokens[5])

    d = dist(lon, lat, curr_lon, curr_lat)
    if name in dists:
        if d < dists[name]:
            dists[name] = d
    else:
        dists[name] = d

nearest = sorted(dists.items(), key=lambda x: x[1])[0][0]
print(nearest)
