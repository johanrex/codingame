def sum_of_digits(n):
    s_n = str(n)
    s = 0
    for i in s_n:
        s += int(i)

    return s
