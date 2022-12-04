import argparse
import glob
import os
import re


pat1 = re.compile(r"import (.*)", re.MULTILINE)
pat2 = re.compile(r"from (.*) import ", re.MULTILINE)


# parser = argparse.ArgumentParser(prog="Make one file", description="Makes one file from many python files", epilog="...")
# parser.add_argument("-i", "--ignore")
# parser.add_argument("folder")
# args = parser.parse_args()

# # read all python files in folder.
# paths = glob.glob(args.folder + "/*.py")

paths = [
    "death-first-search-ep2\\log.py",
    "death-first-search-ep2\\graph.py",
    "death-first-search-ep2\\solution.py",
    "death-first-search-ep2\\main.py",
]

module_names = [os.path.splitext(os.path.basename(path))[0] for path in paths]

big = ""
for path in paths:
    with open(path, "r") as f:
        for line in f:
            if (m := re.search(pat2, line)) is not None:
                if m.group(1) in module_names:
                    continue
            else:
                if (m := re.search(pat1, line)) is not None:
                    if m.group(1) in module_names:
                        continue

            big += line


output_filename = "big.py"
with open(output_filename, "w") as f:
    f.write(big)
