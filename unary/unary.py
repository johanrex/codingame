def log(*objects):
    import sys

    print(*objects, file=sys.stderr, flush=True)


def logged_input():
    s = input()
    log("INPUT:", s)
    return s


def to_bin(s):
    ans = ""
    for c in s:
        ans += format(ord(c), "b").zfill(7)
    return ans


def count_same(s, start_pos) -> int:
    count = 0
    for i in range(start_pos, len(s)):
        if s[i] == s[start_pos]:
            count += 1
        else:
            break
    return count


def encode(s):
    result = ""
    b = to_bin(s)

    i = 0
    while i < len(b):
        count = count_same(b, i)
        result += ("0" if b[i] == "1" else "00") + " "
        result += "0" * count + " "
        i += count
    result = result.rstrip()
    return result


if __name__ == "__main__":

    msg = logged_input()
    ans = encode(msg)
    print(ans)
