import sys
from pathlib import Path

#silly stuff in order to import the main.py module
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import State

def test_next_state():
    s1 = State.get_empty_board_state()
    s2 = s1._State__next_state(0, 0)
    print(str(s2))
    s3 = s2._State__next_state(0, 1)
    print(str(s3))
    s4 = s3._State__next_state(0, 1)
    print(str(s4))


    tmp = State.get_empty_board_state()
    for i in range(8):
        tmp = tmp._State__next_state(0, 1)
        print(tmp)

    pass

if __name__ == "__main__":
    test_next_state()
