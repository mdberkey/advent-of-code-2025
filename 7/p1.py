
with open("input") as f:
    res = 0
    lines = [line.strip() for line in f]
    start = lines[0].index("S")
    beams = set()
    beams.add(start)

    for row in lines[1:]:
        for j in range(len(row)):
            if row[j] == "^" and j in beams:
                if j > 0:
                    beams.add(j - 1)
                if j < len(row):
                    beams.add(j + 1)
                beams.remove(j)
                res += 1

    print(res)
