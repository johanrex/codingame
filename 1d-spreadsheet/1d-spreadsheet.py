import sys

OP_VALUE = "VALUE"
OP_ADD = "ADD"
OP_SUB = "SUB"
OP_MULT = "MULT"


def log(*objects):
    # debug-logging in codingame is defined like this.
    print(*objects, file=sys.stderr, flush=True)


def logged_input():
    s = input()
    log("INPUT:", s)
    return s


def is_ref(arg):
    if isinstance(arg, str):
        return arg[0] == "$"


def evaluate(cells, memo, ref_id):
    if ref_id not in memo:
        operation, arg1, arg2 = cells[ref_id]
        log(f"evaluating {ref_id}: {operation} {arg1} {arg2}")

        if is_ref(arg1):
            arg_ref_id = int(arg1[1:])
            arg1 = evaluate(cells, memo, arg_ref_id)

        if is_ref(arg2):
            arg_ref_id = int(arg2[1:])
            arg2 = evaluate(cells, memo, arg_ref_id)

        arg1 = int(arg1)

        if operation == OP_VALUE:
            value = arg1
        else:
            arg2 = int(arg2)
            if operation == OP_ADD:
                value = arg1 + arg2
            elif operation == OP_SUB:
                value = arg1 - arg2
            elif operation == OP_MULT:
                value = arg1 * arg2
            else:
                raise ValueError(f"Unknown operation: {operation}")

        memo[ref_id] = value
    return memo[ref_id]


cells = []
n = int(input())
for i in range(n):
    operation, arg1, arg2 = logged_input().split()
    cells.insert(i, (operation, arg1, arg2))

memo = {}
for i in range(n):
    print(evaluate(cells, memo, i))
