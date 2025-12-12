import math
from functools import lru_cache

with open("input") as f:
    lines = [line.strip() for line in f]
    res = 0

    for l in lines:
        items = l.split()
        buttons = items[1:-1]
        but_nums = []
        target = []

        for char in items[0][1:-1]:
            if char == ".":
                target.append(0)
            else:
                target.append(1)
        for but in buttons:
            but_nums.append([int(num) for num in but[1:-1].split(",")])

        @lru_cache(maxsize=None)
        def dfs(i, curr_config):
            curr_config = list(curr_config)
            if i == len(but_nums):
                return 0 if curr_config == target else math.inf
            skip = dfs(i + 1, tuple(curr_config))
            for num in but_nums[i]:
                curr_config[num] ^= 1
            return min(skip, 1 + dfs(i + 1, tuple(curr_config)))

        res += dfs(0, (0,) * len(target))

    print(res)
        