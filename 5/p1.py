
with open("input") as f:
    res = 0
    ranges = []
    ids = []
    is_range = True

    for line in f:
        if is_range and len(line) < 3:
            is_range = False
        elif is_range:
            n1, n2 = line.split("-")
            ranges.append((int(n1), int(n2)))
        else:
            for n1, n2 in ranges:
                if n1 <= int(line) <= n2:
                    res += 1
                    break

    print(res)
