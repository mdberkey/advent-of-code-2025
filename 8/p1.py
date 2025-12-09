import math
from collections import Counter

with open("input") as f:
    lines = [line.strip() for line in f]
    box_tups = []
    for i in range(len(lines)):
        b1 = tuple([int(num) for num in lines[i].split(",")])
        for j in range(i + 1, len(lines)):
            b2 = tuple([int(num) for num in lines[j].split(",")])
            dist = math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2)
            box_tups.append((dist, b1, b2))
    
    box_tups.sort(key=lambda x : x[0])        
    box_id_map = {}
    for i, (_, b1, b2) in enumerate(box_tups):
        i += 1
        box_id_map[b1] = i
        box_id_map[b2] = -i
    
    for i, (dist, b1, b2) in enumerate(box_tups):
        if i == 1000:
            break
        if box_id_map[b1] == box_id_map[b2]:
            continue

        new_set_id = box_id_map[b1]
        old_set_id = box_id_map[b2]
        for box, set_id in box_id_map.items():
            if set_id == old_set_id:
                box_id_map[box] = new_set_id
    
    set_sizes = Counter(box_id_map.values())
    sorted_sizes = sorted([val for val in set_sizes.values()], reverse=True)
    print(sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2])
