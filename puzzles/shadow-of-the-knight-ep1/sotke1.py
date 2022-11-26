import sys
import math


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def log_state(x, y, direction, x_min, x_max, y_min, y_max):
    log(f"x_min: {x_min}")
    log(f"x_max: {x_max}")
    log(f"y_min: {y_min}")
    log(f"y_max: {y_max}")
    log(f"x: {x}")
    log(f"y: {y}")
    log(direction)


def move(x, y, direction, x_min, x_max, y_min, y_max):
    log("State before move:")
    log_state(x, y, direction, x_min, x_max, y_min, y_max)

    if "U" in direction:
        y_max = y
        y -= math.ceil((y - y_min) / 2)
    elif "D" in direction:
        y_min = y
        y += math.ceil((y_max - y) / 2)

    if "L" in direction:
        x_max = x
        x -= math.ceil((x - x_min) / 2)
    elif "R" in direction:
        x_min = x
        x += math.ceil((x_max - x) / 2)

    log("State after move:")
    log_state(x, y, direction, x_min, x_max, y_min, y_max)

    return x, y, x_min, x_max, y_min, y_max


def main():
    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x, y = [int(i) for i in input().split()]

    x_min = 0
    x_max = w - 1

    y_min = 0
    y_max = h - 1

    log(f"w:{w}. h:{h}.")

    # game loop
    while True:
        direction = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

        x, y, x_min, x_max, y_min, y_max = move(x, y, direction, x_min, x_max, y_min, y_max)

        # the location of the next window Batman should jump to.
        print(f"{x} {y}")


if __name__ == "__main__":
    main()


def test():

    x = 0
    y = 9
    direction = "U"
    x_min = 0
    x_max = 9
    y_min = 0
    y_max = 9
    x, y, x_min, x_max, y_min, y_max = move(x, y, direction, x_min, x_max, y_min, y_max)
    x, y, x_min, x_max, y_min, y_max = move(x, y, direction, x_min, x_max, y_min, y_max)
    x, y, x_min, x_max, y_min, y_max = move(x, y, direction, x_min, x_max, y_min, y_max)
    x, y, x_min, x_max, y_min, y_max = move(x, y, direction, x_min, x_max, y_min, y_max)
    x, y, x_min, x_max, y_min, y_max = move(x, y, direction, x_min, x_max, y_min, y_max)


# test()
