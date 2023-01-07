content = """
INPUT: 2
INPUT: **********
INPUT: *----P---*
INPUT: *--------*
INPUT: *--------*
INPUT: *-*****--*
INPUT: *-----E--*
INPUT: *--------*
INPUT: *--------*
INPUT: *--------*
INPUT: **********
INPUT: 5 6
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

name = "01_EZ"
write_test_files(content, "tests/test_files/" + name + "_input.txt", "tests/test_files/" + name + "_output.txt")
