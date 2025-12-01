
with open("input") as f:
    
    res = 0
    curr = 50
    for line in f:
        side, val = line[0], int(line[1:])
        step = 1 if side == "R" else -1

        for i in range(val):
            curr = (curr + step) % 100
            if curr == 0:
                res += 1
        
    print(res)
