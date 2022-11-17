from dataclasses import dataclass
import sys
import math


@dataclass
class Checkpoint:
    x: int
    y: int


def log(msg):
    import sys

    print(msg, file=sys.stderr, flush=True)


def get_checkpoint_starting_at_longest_straight(checkpoints):

    log("Checkpoints:")
    log(checkpoints)

    lst_distances = []

    for i in range(1, len(checkpoints)):
        a = checkpoints[i - 1]
        b = checkpoints[i]

        dist = math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
        lst_distances.append((dist, a))  # distance and start point.

    lst_distances.sort()
    log(lst_distances)

    tpl = lst_distances[-1]
    log("Starting at:")
    log(tpl)

    longest_straight_starts_at_checkpoint = tpl[1]

    return longest_straight_starts_at_checkpoint


checkpoints = []
prev_checkpoint = None
boost_checkpoint = None

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    checkpoint = Checkpoint(next_checkpoint_x, next_checkpoint_y)
    if checkpoint not in checkpoints:
        # collect checkpoints
        checkpoints.append(checkpoint)

    if prev_checkpoint is not None and checkpoint != prev_checkpoint:
        # We have completed one lap of the circuit if we reach this.
        boost_checkpoint = get_checkpoint_starting_at_longest_straight(checkpoints)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    # print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 80")

    if boost_checkpoint is not None and checkpoint == boost_checkpoint:
        thrust = "BOOST"
    else:
        if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
            thrust = 0
        else:
            thrust = 100

    cmd = f"{next_checkpoint_x} {next_checkpoint_y} {thrust}"
    print(cmd)
