
with open("input") as f:
    res = 0
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    grid = []
    for line in f:
        grid.append(list(line.strip()))

    def is_inbounds(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        return True

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "@":
                continue
            count = 0
            
            for dr, dc in DIRECTIONS:
                if is_inbounds(i + dr, j + dc) and grid[i+dr][j+dc] == "@":
                    count +=1
            
            if count < 4:
                res += 1
    
    print(res)
