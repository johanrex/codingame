content = """
Standard Error Stream:

INPUT: 10 14 4
INPUT: 2 6
INPUT: 9 7
INPUT: 0 7
INPUT: 9 8
INPUT: 8 2
INPUT: 7 1
INPUT: 9 2
INPUT: 3 1
INPUT: 2 5
INPUT: 0 8
INPUT: 4 1
INPUT: 9 1
INPUT: 0 9
INPUT: 2 1
INPUT: 3
INPUT: 4
INPUT: 5
INPUT: 6
INPUT: 0
OUTPUT: 1 3

Standard Output Stream:

1 3

Game information:

Link [1-3] severed
Agent moved from 0 to 9

1 4
Standard Error Stream:

INPUT: 9
OUTPUT: 2 5

Standard Output Stream:

2 5

Game information:

Link [2-5] severed
Agent moved from 9 to 1

2 4
Standard Error Stream:

INPUT: 1
OUTPUT: 1 4

Standard Output Stream:

1 4

Game information:

Link [1-4] severed
Agent moved from 1 to 2

3 4
Standard Error Stream:

INPUT: 2
OUTPUT: 2 6
"""

def extract(content, prefix):
    return [line[len(prefix):] for line in content if line.startswith(prefix)]

def write(lines:list[str], path:str):
    lines.append("") #add the empty last line.
    with open(path, "w") as f:
        f.write("\n".join(lines))

def write_test_files(content, input_filename, output_filename):
    input_lines = extract(content, "INPUT: ")
    output_lines = extract(content, "OUTPUT: ")

    write(input_lines, input_filename)
    write(output_lines, output_filename)

content = content.split("\n")

name = "02_linked_double_gateways"
write_test_files(content, "tests/test_files/" + name + "_input.txt", "tests/test_files/" + name + "_output.txt")
