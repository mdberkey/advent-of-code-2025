
with open("input") as f:
    res = 0
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    grid = [list(line.strip()) for line in f]
    
    def is_out_of_bounds(i, j):
        return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])
    
    flag = False
    while not flag:
        flag = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "@":
                    continue
                count = 0

                for dr, dc in DIRECTIONS:
                    if not is_out_of_bounds(i + dr, j + dc) and grid[i+dr][j+dc] == "@":
                        count +=1
                
                if count < 4:
                    res += 1
                    grid[i][j] = "."
                    flag = False

    print(res)
