
# code is broken since answer is too low
with open("input") as f:
    points = [tuple(map(int, line.strip().split(",")))[::-1] for line in f]
    points.append(points[0])
    res = 0
    shape_lines = []

    def lines_intersect(l1, l2, dir):
        if l1[0] == l2[0] or l1[0] == l2[1] or l1[1] == l2[0] or l1[1] == l2[1]:
            return False
        (l1y1, l1x1), (l1y2, l1x2) = l1
        (l2y1, l2x1), (l2y2, l2x2) = l2
        l1_vert = (l1x1 == l1x2)
        l2_vert = (l2x1 == l2x2)

        if l1_vert == l2_vert:
            return False

        if l1_vert:
            if min(l2x1, l2x2) <= l1x1 <= max(l2x1, l2x2):
                if min(l1y1, l1y2) <= l2y1 <= max(l1y1, l1y2): 
                    if dir == (0, -1) and max(l2x1, l2x2) > l1x1:
                        return True
                    if dir == (0, 1) and min(l2x1, l2x2) < l1x1:
                        return True
        if l2_vert:
            if min(l1x1, l1x2) <= l2x1 <= max(l1x1, l1x2):
                if min(l2y1, l2y2) <= l1y1 <= max(l2y1, l2y2): 
                    if dir == (-1, 0) and max(l2y1, l2y2) > l1y1:
                        return True
                    if dir == (1, 0) and max(l2y1, l2y2) > l1y1:
                        return True
        return False

    for i in range(1, len(points)):
        shape_lines.append((points[i-1], points[i]))
    
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            tl = (min(p1[0], p2[0]), min(p1[1], p2[1]))
            tr = (min(p1[0], p2[0]), max(p1[1], p2[1]))
            bl = (max(p1[0], p2[0]), min(p1[1], p2[1]))
            br = (max(p1[0], p2[0]), max(p1[1], p2[1]))

            valid = True
            for sl in shape_lines:
                if (lines_intersect((tl, tr), sl, (-1, 0)) or # up
                    lines_intersect((tr, br), sl, (0, 1)) or # right
                    lines_intersect((br, bl), sl, (1, 0)) or # bot 
                    lines_intersect((bl, tl), sl, (0, -1))): # left
                    valid = False
                    break
            
            if valid:
                res = max(res, (br[1] - bl[1] + 1) * (br[0] - tl[0] + 1))
    
    print(res)
