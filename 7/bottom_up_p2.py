
with open("input") as f:
    lines = [line.strip() for line in f]
    memo = [[0] * len(lines[0])] + [[1] * len(lines[0])]

    for i in range(len(lines) - 1, -1, -1):
        for j in range(len(lines[0])):
            if lines[i][j] == "^":
                memo[0][j] = memo[1][j-1] + memo[1][j+1]
            else:
                memo[0][j] = memo[1][j]
        for j in range(len(lines[0])):
            memo[1][j] = memo[0][j]
        
    print(memo[0][lines[0].index("S")])
