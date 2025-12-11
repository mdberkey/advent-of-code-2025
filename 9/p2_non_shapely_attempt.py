# # also store corner red tile pairs in list.
# # create grid of True bools with +1 row and col for padding
# # do dfs floodfill at 0,0 and set outside to False
# # check each pair of red tiles, check that each edge is in grid.
# # return max
# # idk, need to get a hint or something

# # so efficiencty issue is that it can't store all points.
# # what about storing just "lines"? idk.

# # need a way to compress coordinates, then do line intersection.

# # what if, store each line with start and stop.
# # iterate squares
# # check if a line interesects or not.
# # why can't I just do that with lines?

# # so new strat, basically check if lines intersect
# # how to tell if lines of rect intersect with shape?
# # could maybe store all points for each line, then check for intersection...
# # basically, store all shape coords in set.
# # iterate rects, then check if any rect line intersects. How?
# # only happens if a rect shares a point with a line and they're going in diff
# # directiosn right?

# # need to find strict intersections. Basically if any lines cross each other
# # and it's not the endpoint of either shape. 

# # so basically check for intersections between input lines and rectangle
# # how? get slope. If opposite slope, check if vert line col between
# # horizontal line cols and if hor line row between vert (and not on endpoint)

# # get points for each line in polygon. arr[(p1, p2)]
# # iterate rects, check if lines intersect using algo. return max


# with open("input") as f:
#     points = [tuple(map(int, line.strip().split(",")))[::-1] for line in f]
#     points.append(points[0])
#     res = 0
#     shape_lines = []

#     def lines_intersect(l1, l2, dir):
#         if l1[0] == l2[0] or l1[0] == l2[1] or l1[1] == l2[0] or l1[1] == l2[1]:
#             return False
#         (l1y1, l1x1), (l1y2, l1x2) = l1
#         (l2y1, l2x1), (l2y2, l2x2) = l2
#         l1_vert = (l1x1 == l1x2)
#         l2_vert = (l2x1 == l2x2)

#         if l1_vert == l2_vert:
#             return False

#         if l1_vert:
#             if min(l2x1, l2x2) <= l1x1 <= max(l2x1, l2x2):
#                 if min(l1y1, l1y2) <= l2y1 <= max(l1y1, l1y2): 
#                     if dir == (0, -1) and max(l2x1, l2x2) > l1x1: # left
#                         return True
#                     if dir == (0, 1) and min(l2x1, l2x2) < l1x1: # right
#                         return True
#         if l2_vert:
#             if min(l1x1, l1x2) <= l2x1 <= max(l1x1, l1x2):
#                 if min(l2y1, l2y2) <= l1y1 <= max(l2y1, l2y2): 
#                     if dir == (-1, 0) and max(l2y1, l2y2) > l1y1: # left
#                         return True
#                     if dir == (1, 0) and max(l2y1, l2y2) > l1y1: # left
#                         return True
#         return False

#     for i in range(1, len(points)):
#         shape_lines.append((points[i-1], points[i]))
    
#     for i, p1 in enumerate(points):
#         for p2 in points[i+1:]:
#             tl = (min(p1[0], p2[0]), min(p1[1], p2[1]))
#             tr = (min(p1[0], p2[0]), max(p1[1], p2[1]))
#             bl = (max(p1[0], p2[0]), min(p1[1], p2[1]))
#             br = (max(p1[0], p2[0]), max(p1[1], p2[1]))

#             valid = True
#             for sl in shape_lines:
#                 if (lines_intersect((tl, tr), sl, (-1, 0)) or # up
#                     lines_intersect((tr, br), sl, (0, 1)) or # right
#                     lines_intersect((br, bl), sl, (1, 0)) or # bot 
#                     lines_intersect((bl, tl), sl, (0, -1))): # left
#                     valid = False
#                     break
            
#             if valid:
#                 res = max(res, (br[1] - bl[1] + 1) * (br[0] - tl[0] + 1))
    
#     print(res)

#     # answer is too low:   287978571
#     # answer is too high: 2427373160
#     # not answer,          407898990
#     # answer?:            1534043700 
#     #                     1534043700                    
#     # took like 30 sec too
