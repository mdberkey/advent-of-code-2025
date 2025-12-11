
with open("input") as f:
    lines = [line.strip() for line in f]
    res = 0

    for i, line in enumerate(lines):
        c, r = map(int, line.split(","))
        for j, line2 in enumerate(lines[i+1:]):
            c2, r2 = map(int, line2.split(","))

            res = max(res, abs(r - r2 + 1) * abs(c - c2 + 1))

    print(res)