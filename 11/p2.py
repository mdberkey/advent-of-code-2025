from collections import defaultdict
from functools import lru_cache

with open("input") as f:
    lines = [line.strip() for line in f]
    res = 0
    graph = defaultdict(list)

    for line in lines:
        device, adjs = line.split(": ")
        graph[device] = adjs.split(" ")

    @lru_cache(maxsize=None)
    def dfs_backtracking(device, seen_dac, seen_fft):
        if device == "out":
            return 1 if seen_dac and seen_fft else 0
        elif device == "dac":
            seen_dac = True
        elif device == "fft":
            seen_fft = True
        
        val = 0
        for adj in graph[device]:
            val += dfs_backtracking(adj, seen_dac, seen_fft)
        
        return val

    print(dfs_backtracking("svr", False, False))
    