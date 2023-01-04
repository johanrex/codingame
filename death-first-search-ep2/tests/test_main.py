
#test_main.py:
import sys
from pathlib import Path

#silly stuff in order to import the main.py module
sys.path.insert(0, str(Path(__file__).parent.parent))
import main


class MockIO:
    def __init__(self, input_path, output_path):
        
        with open(input_path, "r") as f:
            self.input_lines = [line.strip() for line in f.readlines()]

        with open(output_path, "r") as f:
            self.output_lines = [line.strip() for line in f.readlines()]

        self.input_file_index = 0
        self.output_file_index = 0

    def mock_input(self, prompt=None):
        if self.input_file_index >= len(self.input_lines):
            raise EOFError

        line = self.input_lines[self.input_file_index]
        self.input_file_index += 1
        return line

    def mock_print(self, *args, **kwargs):
        if self.output_file_index >= len(self.output_lines):
            raise EOFError

        line = self.output_lines[self.output_file_index]
        self.output_file_index += 1
        assert line == " ".join([str(arg) for arg in args])
        print(*args, **kwargs)

def test_main_robust_double_gateways():
    mock_io = MockIO("tests/test_files/01_robust_double_gateways_input.txt", "tests/test_files/01_robust_double_gateways_output.txt")
    main.main(mock_io.mock_input, mock_io.mock_print)
    

def test_main_ordered_gateways():
    mock_io = MockIO("tests/test_files/04_ordered_gateways_input.txt", "tests/test_files/04_ordered_gateways_output.txt")
    main.main(mock_io.mock_input, mock_io.mock_print)


def test_main_02_linked_double_gateways_input():
    mock_io = MockIO("tests/test_files/02_linked_double_gateways_input.txt", "tests/test_files/02_linked_double_gateways_output.txt")
    main.main(mock_io.mock_input, mock_io.mock_print)



if __name__ == "__main__":
    test_main_robust_double_gateways()
    test_main_ordered_gateways()
    