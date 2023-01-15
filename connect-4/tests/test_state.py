import sys
from pathlib import Path

#silly stuff in order to import the main.py module
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import State

def test_next_state():
    state = State.get_empty_board_state()
    next_state = state._State__next_state(0, 0)
    print(str(next_state))


if __name__ == "__main__":
    test_next_state()
