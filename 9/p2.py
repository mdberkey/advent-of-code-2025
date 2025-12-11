from shapely.geometry import Polygon, box
from shapely.prepared import prep
from itertools import combinations

with open("input") as f:
    points = [tuple(map(int, line.strip().split(",")))[::-1] for line in f]
    res = 0

    rects = []
    for (x1, y1), (x2, y2) in combinations(points, 2):
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        area = (max_x - min_x + 1) * (max_y - min_y + 1)
        rects.append((area, min_x, min_y, max_x, max_y))
    
    rects.sort(key=lambda x: -x[0])
    shape = prep(Polygon(points).simplify(0))

    for area, min_x, min_y, max_x, max_y in rects:
        if shape.covers(box(min_x, min_y, max_x, max_y)):
            print(area)
            break
    