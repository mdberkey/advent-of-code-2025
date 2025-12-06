
with open("input") as f:
    res = 0
    ranges = []

    for line in f:
        if len(line) < 3:
            break
        n1, n2 = line.split("-")
        ranges.append((int(n1), int(n2)))
    
    ranges.sort()
    merged_ranges = []
    l, r = ranges[0]
    for n1, n2 in ranges[1:]:
        if n1 > r:
            merged_ranges.append((l, r))
            l = n1
            r = n2
        else:
            r = max(r, n2)
    merged_ranges.append((l, r))
    
    for n1, n2 in merged_ranges:
        res += n2 - n1 + 1

    print(res)
