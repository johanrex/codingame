content = """
INPUT: 49 62 17
INPUT: 1 0
INPUT: 1 2
INPUT: 2 3
INPUT: 3 4
INPUT: 4 5
INPUT: 3 6
INPUT: 7 3
INPUT: 9 5
INPUT: 5 8
INPUT: 13 0
INPUT: 14 13
INPUT: 15 14
INPUT: 16 13
INPUT: 17 14
INPUT: 18 15
INPUT: 19 15
INPUT: 19 20
INPUT: 19 18
INPUT: 18 20
INPUT: 22 20
INPUT: 0 23
INPUT: 23 14
INPUT: 23 16
INPUT: 21 20
INPUT: 24 21
INPUT: 24 17
INPUT: 28 27
INPUT: 27 29
INPUT: 27 26
INPUT: 26 25
INPUT: 25 21
INPUT: 21 30
INPUT: 30 34
INPUT: 31 35
INPUT: 32 36
INPUT: 38 33
INPUT: 33 37
INPUT: 33 32
INPUT: 32 31
INPUT: 31 30
INPUT: 33 39
INPUT: 9 40
INPUT: 39 40
INPUT: 41 2
INPUT: 39 42
INPUT: 42 43
INPUT: 43 10
INPUT: 34 46
INPUT: 35 45
INPUT: 37 40
INPUT: 41 46
INPUT: 44 45
INPUT: 44 40
INPUT: 7 41
INPUT: 5 10
INPUT: 47 12
INPUT: 11 47
INPUT: 10 47
INPUT: 43 47
INPUT: 46 48
INPUT: 45 48
INPUT: 48 7
INPUT: 6
INPUT: 7
INPUT: 8
INPUT: 9
INPUT: 11
INPUT: 12
INPUT: 16
INPUT: 17
INPUT: 18
INPUT: 22
INPUT: 28
INPUT: 29
INPUT: 34
INPUT: 35
INPUT: 36
INPUT: 37
INPUT: 38
INPUT: 0
OUTPUT: 33 37

Standard Output Stream:

33 37

Game information:

Link [33-37] severed
Agent moved from 0 to 13

1 6
Standard Error Stream:

INPUT: 13
OUTPUT: 13 16

Standard Output Stream:

13 16

Game information:

Link [13-16] severed
Agent moved from 13 to 14

2 6
Standard Error Stream:

INPUT: 14
OUTPUT: 14 17

Standard Output Stream:

14 17

Game information:

Link [14-17] severed
Agent moved from 14 to 15

3 6
Standard Error Stream:

INPUT: 15
OUTPUT: 15 18

Standard Output Stream:

15 18

Game information:

Link [15-18] severed
Agent moved from 15 to 19

4 6
Standard Error Stream:

INPUT: 19
OUTPUT: 19 18

Standard Output Stream:

19 18

Game information:

Link [19-18] severed
Agent moved from 19 to 20

5 6
Standard Error Stream:

INPUT: 20
OUTPUT: 20 18

Standard Output Stream:

20 18
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

name = "06_bobnet_core_network"
write_test_files(content, "tests/test_files/" + name + "_input.txt", "tests/test_files/" + name + "_output.txt")
