
with open("input") as f:
    lines = [line.strip() for line in f]
    res = 0

    for l in lines[30:]:
        size, tile_counts = l.split(": ")
        size = list(map(int, size.split("x")))
        t_num = sum(list(map(int, tile_counts.split()))) * 7

        if t_num < size[0] * size[1]:
            res += 1
    
    print(res)
