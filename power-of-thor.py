r = input

lx, ly, tx, ty = [int(i) for i in r().split()]

while True:
    r()

    d = ""
    if ly > ty:
        ty += 1
        d += "S"
    elif ly < ty:
        ty -= 1
        d += "N"

    if lx > tx:
        tx += 1
        d += "E"
    if lx < tx:
        tx -= 1
        d += "W"

    print(d)
