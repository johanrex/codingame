import sys


def log(*objects):
    import sys

    print(*objects, file=sys.stderr, flush=True)


def logged_input():
    s = input()
    log("INPUT:", s)
    return s


def get_shape(grid):
    return len(grid[0]), len(grid)


def get_start_pos(grid):
    w, h = get_shape(grid)
    pos = (-1, -1)
    for x in range(w):
        for y in range(h):
            if grid[y][x] == "S":
                pos = (x, y)
    assert pos != (-1, -1)
    return pos


def read_input():
    w, h = [int(i) for i in logged_input().split()]
    grid = []
    for _ in range(h):
        row = logged_input()
        grid.append(row)

    assert w, h == get_shape(grid)
    return grid


def traverse(from_pos, curr_pos, grid, dist):
    if from_pos is None:
        # current pos is the starting pos.
        dist[curr_pos] = 0
    else:
        curr_steps = dist[from_pos] + 1

        if curr_pos in dist:
            existing_steps = dist[curr_pos]
        else:
            existing_steps = sys.maxsize

        if curr_steps < existing_steps:
            dist[curr_pos] = curr_steps
        else:
            return

    # get_available_pos...
    for pos in get_available_pos(from_pos, curr_pos, grid):
        traverse(curr_pos, pos, grid, dist)


def get_available_pos(from_pos, current_pos, grid):
    poss = []
    curr_x, curr_y = current_pos
    poss.append((curr_x - 1, curr_y))
    poss.append((curr_x + 1, curr_y))
    poss.append((curr_x, curr_y - 1))
    poss.append((curr_x, curr_y + 1))

    w, h = get_shape(grid)
    # fix min/max
    for i in range(len(poss)):
        x, y = poss[i]
        x = x % w
        y = y % h
        poss[i] = (x, y)

    poss = [(x, y) for (x, y) in poss if grid[y][x] != "#" and (x, y) != from_pos]
    return poss


def distance_to_str_repr(d):
    ret = ""
    if d < 10:
        ret = str(d)
    else:
        ret = chr(65 - 10 + d)

    return ret


def print_result(grid, dist):

    w, h = get_shape(grid)
    for y in range(h):
        arr = bytearray(grid[y], encoding="utf-8")
        for x in range(w):
            pos = (x, y)
            if pos in dist:
                s = distance_to_str_repr(dist[pos])
                arr[x] = ord(s)
        print(arr.decode("utf-8"))


def main():
    grid = read_input()
    start_pos = get_start_pos(grid)
    dist = {}
    traverse(None, start_pos, grid, dist)
    print_result(grid, dist)


if __name__ == "__main__":
    main()
