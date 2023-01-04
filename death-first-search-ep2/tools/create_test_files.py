content = """
Standard Error Stream:

INPUT: 37 81 4
INPUT: 2 5
INPUT: 14 13
INPUT: 16 13
INPUT: 19 21
INPUT: 13 7
INPUT: 16 8
INPUT: 35 5
INPUT: 2 35
INPUT: 10 0
INPUT: 8 3
INPUT: 23 16
INPUT: 0 1
INPUT: 31 17
INPUT: 19 22
INPUT: 12 11
INPUT: 1 2
INPUT: 1 4
INPUT: 14 9
INPUT: 17 16
INPUT: 30 29
INPUT: 32 22
INPUT: 28 26
INPUT: 24 23
INPUT: 20 19
INPUT: 15 13
INPUT: 18 17
INPUT: 6 1
INPUT: 29 28
INPUT: 15 14
INPUT: 9 13
INPUT: 32 18
INPUT: 25 26
INPUT: 1 7
INPUT: 34 35
INPUT: 33 34
INPUT: 27 16
INPUT: 27 26
INPUT: 23 25
INPUT: 33 3
INPUT: 16 30
INPUT: 25 24
INPUT: 3 2
INPUT: 5 4
INPUT: 31 32
INPUT: 27 25
INPUT: 19 3
INPUT: 17 8
INPUT: 4 2
INPUT: 32 17
INPUT: 10 11
INPUT: 29 27
INPUT: 30 27
INPUT: 6 4
INPUT: 24 15
INPUT: 9 10
INPUT: 34 2
INPUT: 9 7
INPUT: 11 6
INPUT: 33 2
INPUT: 14 10
INPUT: 12 6
INPUT: 0 6
INPUT: 19 17
INPUT: 20 3
INPUT: 21 20
INPUT: 21 32
INPUT: 15 16
INPUT: 0 9
INPUT: 23 27
INPUT: 11 0
INPUT: 28 27
INPUT: 22 18
INPUT: 3 1
INPUT: 23 15
INPUT: 18 19
INPUT: 7 0
INPUT: 19 8
INPUT: 21 22
INPUT: 7 36
INPUT: 13 36
INPUT: 8 36
INPUT: 0
INPUT: 16
INPUT: 18
INPUT: 26
INPUT: 2
OUTPUT: 27 16

Standard Output Stream:

27 16

Game information:

Link [27-16] severed
Agent moved from 2 to 1

01 20
Standard Error Stream:

INPUT: 1
OUTPUT: 1 0

Standard Output Stream:

1 0

Game information:

Link [1-0] severed
Agent moved from 1 to 7

02 20
Standard Error Stream:

INPUT: 7
OUTPUT: 7 0

Standard Output Stream:

7 0

Game information:

Link [7-0] severed
Agent moved from 7 to 13

03 20
Standard Error Stream:

INPUT: 13
OUTPUT: 13 16

Standard Output Stream:

13 16

Game information:

Link [13-16] severed
Agent moved from 13 to 15

04 20
Standard Error Stream:

INPUT: 15
OUTPUT: 15 16

Standard Output Stream:

15 16

Game information:

Link [15-16] severed
Agent moved from 15 to 23

05 20
Standard Error Stream:

INPUT: 23
OUTPUT: 23 16

Standard Output Stream:

23 16

Game information:

Link [23-16] severed
Agent moved from 23 to 27

06 20
Standard Error Stream:

INPUT: 27
OUTPUT: 27 26

Standard Output Stream:

27 26

Game information:

Link [27-26] severed
Agent moved from 27 to 30

07 20
Standard Error Stream:

INPUT: 30
OUTPUT: 30 16

Standard Output Stream:

30 16

Game information:

Link [30-16] severed
Agent moved from 30 to 27

08 20
Standard Error Stream:

INPUT: 27
OUTPUT: 17 16

Standard Output Stream:

17 16

Game information:

Link [17-16] severed
Agent moved from 27 to 25

09 20
Standard Error Stream:

INPUT: 25
OUTPUT: 25 26

Standard Output Stream:

25 26

Game information:

Link [25-26] severed
Agent moved from 25 to 27

10 20
Standard Error Stream:

INPUT: 27
OUTPUT: 10 0

Standard Output Stream:

10 0

Game information:

Link [10-0] severed
Agent moved from 27 to 28

11 20
Standard Error Stream:

INPUT: 28
OUTPUT: 28 26

Standard Output Stream:

28 26

Game information:

Link [28-26] severed
Agent moved from 28 to 27

12 20
Standard Error Stream:

INPUT: 27
OUTPUT: 6 0

Standard Output Stream:

6 0

Game information:

Link [6-0] severed
Agent moved from 27 to 23

13 20
Standard Error Stream:

INPUT: 23
OUTPUT: 9 0

Standard Output Stream:

9 0

Game information:

Link [9-0] severed
Agent moved from 23 to 15

14 20
Standard Error Stream:

INPUT: 15
OUTPUT: 11 0

Standard Output Stream:

11 0

Game information:

Link [11-0] severed
Agent moved from 15 to 13

15 20
Standard Error Stream:

INPUT: 13
OUTPUT: 8 16

Standard Output Stream:

8 16

Game information:

Link [8-16] severed
Agent moved from 13 to 36

16 20
Standard Error Stream:

INPUT: 36
OUTPUT: 17 18

Standard Output Stream:

17 18

Game information:

Link [17-18] severed
Agent moved from 36 to 8

17 20
Standard Error Stream:

INPUT: 8
OUTPUT: 32 18

Standard Output Stream:

32 18

Game information:

Link [32-18] severed
Agent moved from 8 to 19

18 20
Standard Error Stream:

INPUT: 19
OUTPUT: 19 18

Standard Output Stream:

19 18

Game information:

Link [19-18] severed
Agent moved from 19 to 22

19 20
Standard Error Stream:

INPUT: 22
OUTPUT: 22 18

Standard Output Stream:

22 18
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

name = "05_complex_mesh"
write_test_files(content, "tests/test_files/" + name + "_input.txt", "tests/test_files/" + name + "_output.txt")
