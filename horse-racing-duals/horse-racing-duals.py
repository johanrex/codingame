import sys

nrs = []

n = int(input())
for i in range(n):
    nr = int(input())
    nrs.append(nr)

nrs.sort()

d = sys.maxsize

for i in range(len(nrs)):
    n1 = nrs[i]
    for j in range(i+1, len(nrs)):
        n2 = nrs[j]
        tmp = abs(n1 - n2)
        if tmp > d:
            break
        if tmp < d:
            d = tmp
print(d)
