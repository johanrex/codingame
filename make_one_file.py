import argparse
import glob
import os
import re

pat1 = re.compile(r"import (.*)", re.MULTILINE)
pat2 = re.compile(r"from (.*) import ", re.MULTILINE)

parser = argparse.ArgumentParser(prog="Make one file", description="Makes one file from many python files", epilog="...")
parser.add_argument("files", nargs="+", help="List of files. Separated by space.")
args = parser.parse_args()

files = args.files

module_names = [os.path.splitext(os.path.basename(file))[0] for file in files]

big = ""
for file in files:
    with open(file, "r") as f:
        for line in f:
            if (m := re.search(pat2, line)) is not None:
                if m.group(1) in module_names:
                    continue
            else:
                if (m := re.search(pat1, line)) is not None:
                    if m.group(1) in module_names:
                        continue

            big += line

output_folder = "dist"
output_filename = "big.py"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, output_filename)
with open(output_path, "w") as f:
    f.write(big)

print("Done. Wrote to", output_path)
