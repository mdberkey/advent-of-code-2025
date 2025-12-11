import math
from collections import deque, Counter

with open("input") as f:
    lines = [line.strip() for line in f]
    res = 0

    for i, line in enumerate(lines):
        c, r = line.split(",")
        r = int(r)
        c = int(c)
        for j, line2 in enumerate(lines[i+1:]):
            c2, r2 = line2.split(",")
            r2 = int(r2)
            c2 = int(c2)

            res = max(res, abs(r - r2 + 1) * abs(c - c2 + 1))

    print(res)