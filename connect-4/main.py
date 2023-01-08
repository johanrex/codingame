import sys
import math

# Drop chips in the columns.
# Connect at least 4 of your chips in any direction to win.

# my_id: 0 or 1 (Player 0 plays first)
# opp_id: if your index is 0, this will be 1, and vice versa
my_id, opp_id = [int(i) for i in input().split()]

# game loop
while True:
    turn_index = int(input())  # starts from 0; As the game progresses, first player gets [0,2,4,...] and second player gets [1,3,5,...]
    for i in range(7):
        board_row = input()  # one row of the board (from top to bottom)
    num_valid_actions = int(input())  # number of unfilled columns in the board
    for i in range(num_valid_actions):
        action = int(input())  # a valid column index into which a chip can be dropped
    opp_previous_action = int(input())  # opponent's previous chosen column index (will be -1 for first player in the first turn)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Output a column index to drop the chip in. Append message to show in the viewer.
    print("0")
