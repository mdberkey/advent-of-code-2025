
with open("input") as f:
    lines = [line.strip() for line in f]
    memo = {} # (i, j) -> num of timelines

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        elif i == len(lines) - 1:
            return 1
        elif lines[i][j] == "^":
            memo[(i, j)] = dfs(i + 1, j - 1) + dfs(i + 1, j + 1)
        else:
            memo[(i, j)] = dfs(i + 1, j)

        return memo[(i, j)]

    print(dfs(0, lines[0].index("S"))) 
