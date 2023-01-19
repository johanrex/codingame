import sys
import random
import math

ROW_COUNT = 7
COL_COUNT = 9
STEAL = -2


def log(*objects):
    # debug-logging in codingame is defined like this.
    print(*objects, file=sys.stderr, flush=True)


def logged_input():
    s = input()
    log("logged_input:", s)
    return s


class State:
    def __init__(self, board, is_win=False) -> None:
        self._board: str = board
        self._is_win:bool = is_win

    def __str__(self) -> str:
        s = ""
        for i in range(ROW_COUNT):
            s += self._board[i * COL_COUNT : (i + 1) * COL_COUNT] + "\n"
        return s


    def print_state(self):
        print(self.__str__())

    def _next_state(self, player_id: int, col: int) -> "State":
        assert col >= 0 and col < COL_COUNT
        assert self._board[col] == "."

        next_board = None
        for row in range(ROW_COUNT):
            offset = (ROW_COUNT -1 - row) * COL_COUNT + col
            if self._board[offset] == ".":
                next_board = self._board[: offset] + str(player_id) + self._board[offset+1:]
                break

        next_state = State(next_board)
        return next_state

    def __next_state_steal(self, board: str, player_id: int) -> "State":
        old_id = 0 if player_id == 1 else 1
        board = board.replace(str(old_id), str(player_id))

        state = State(board)
        return state

    def next_states(self, turn_idx: int, player_id: int, valid_columns: list[int]) -> list:
        states = []
        if turn_idx == 0:
            states.append(self.__next_state_steal(self._board, player_id))

        for col in valid_columns:
            next_state = self._next_state(player_id, col)
            if next_state is not None:
                states.append(next_state)

        return states

    def _is_horizontal_win(self, row, col, player_id) -> bool:
        start = col - 3 if col - 3 > 0 else 0
        end = col + 3 if col +3 < COL_COUNT else COL_COUNT - 1
        same_count = 0
        row_offset = (ROW_COUNT -1 - row) * COL_COUNT
        for idx in range(row_offset + start, row_offset + end+1):
            c = self._board[idx]
            if c == str(player_id):
                same_count += 1
                if same_count == 4:
                    return True
            else:
                same_count = 0
        return False

    def is_win(self, row, col, player_id) -> bool:
        if self._is_horizontal_win(row, col, player_id):
            return True


        #vertical
        #diagonal left
        #diagonal right

        #like-count. 

        return False


    @classmethod
    def get_state_from_input(cls) -> "State":
        board = ""
        for _ in range(ROW_COUNT):
            row = logged_input()
            assert len(row) == COL_COUNT
            board += row

        state = State(board)
        return state

    @classmethod
    def get_empty_board_state(cls) -> "State":
        board = "." * ROW_COUNT * COL_COUNT
        state = State(board)

        return state


class TreeNode:
    def __init__(self, value: State, parent: "TreeNode" = None) -> None:
        self.value = value
        self.parent = parent
        self.children: list[TreeNode] = []

    def add_child(self, child: "TreeNode"):
        self.children.append(child)
        child.parent = self

    def is_leaf(self):
        return len(self.children) == 0

    def is_root(self):
        return self.parent is None


def __gen_tree(current_node, level):
    if level == 0:
        return

    current_state = current_node.value
    next_states = current_state.next_states()
    #next_states(self, turn_idx: int, player_id: int, valid_columns: list[int]) -> list:

    for nxt_state in next_states:
        child_node = TreeNode(nxt_state, parent=current_node)
        __gen_tree(child_node, level - 1)


def gen_tree():
    state = State.get_empty_board_state()
    root = TreeNode(state)

    __gen_tree(root, 2)

    return root

def main():
    root = None
    parent = None

    # my_id: 0 or 1 (Player 0 plays first)
    # opp_id: if your index is 0, this will be 1, and vice versa
    #TODO make id str, no point in int when state is stored as string
    my_id, opp_id = [int(i) for i in logged_input().split()]

    root = gen_tree()


    while True:
        turn_index = int(logged_input())  # starts from 0; As the game progresses, first player gets [0,2,4,...] and second player gets [1,3,5,...]
        current_state = State.get_state_from_input()

        current_node = TreeNode(current_state)
        if root is None:
            root = current_node

        num_valid_actions = int(logged_input())  # number of unfilled columns in the board
        valid_columns = []
        for i in range(num_valid_actions):
            col = int(logged_input())  # a valid column index into which a chip can be dropped
            valid_columns.append(col)
        opp_previous_action = int(logged_input())  # opponent's previous chosen column index (will be -1 for first player in the first turn)

        next_states = current_state.next_states(turn_index,my_id, valid_columns)

        for child_state in next_states:
            current_node.add_child(child_state)

        # Output a column index to drop the chip in. Append message to show in the viewer.
        print(random.choice(valid_columns))

if __name__ == "__main__":
    main()

