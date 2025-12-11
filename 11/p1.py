from collections import defaultdict

with open("input") as f:
    lines = [line.strip() for line in f]
    graph = defaultdict(list)

    for line in lines:
        device, adjs = line.split(": ")
        graph[device] = adjs.split(" ")

    def dfs_backtracking(device):
        if device == "out":
            return 1

        val = 0
        for adj in graph[device]:
            val += dfs_backtracking(adj)

        return val

    print(dfs_backtracking("you"))
