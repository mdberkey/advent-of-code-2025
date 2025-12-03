
with open("input") as f:
    res = 0

    for line in f:
        line = line.strip()
        line = [int(num) for num in line]
        max_num = max(line[:-1])
        seen_max = False
        next_num = min(line)

        for num in line:
            if not seen_max and num == max_num:
                seen_max = True
            elif seen_max:
                next_num = max(next_num, num)
        
        res += int(str(max_num) + str(next_num))

    print(res)