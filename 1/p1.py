with open("input") as f:
    
    res = 0
    curr = 50
    for line in f:
        side, val = line[0], int(line[1:])

        if side == "L":
            curr -= val 
        else:
            curr += val
        
        curr %= 100

        if curr == 0:
            res += 1

    print(res)
