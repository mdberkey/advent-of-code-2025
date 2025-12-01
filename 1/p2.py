
with open("input") as f:
    
    res = 0
    curr = 50
    for line in f:
        side, val = line[0], int(line[1:])

        if side == "R":
            for _ in range(val):
                if curr == 99:
                    curr = 0
                    res += 1
                else:
                    curr += 1
        else:
            for i in range(val):
                if curr == 0:
                    curr = 99
                    if i != 0:
                        res += 1
                else:
                    curr -= 1
                    if curr == 0 and i == val - 1:
                        res += 1

    print(res)

