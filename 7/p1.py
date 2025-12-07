
with open("input") as f:
    res = 0
    lines = [line.strip() for line in f]
    beams = { lines[0].index("S") }

    for row in lines[1:]:
        for j in range(len(row)):
            if row[j] == "^" and j in beams:
                beams.add(j - 1)
                beams.add(j + 1)
                beams.remove(j)
                res += 1

    print(res)
