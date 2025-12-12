import numpy as np

with open("input3") as f:
    lines = [line.strip() for line in f]
    res = 0
    tiles = []
    # DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for i in range(1, 31, 5):
        t = []
        for j in range(i, i + 3):
            t.append([1 if char == "#" else 0 for char in lines[j]])
        tiles.append(t)
    tiles = np.array(tiles)

    def get_unique_tile_orientations(tile):
        forms = [np.rot90(tile, k) for k in range(4)] + \
                [np.rot90(tile.T, k) for k in range(4)]

        return np.unique(np.array(forms), axis=0)

    all_tiles = [] # tile_id -> list of unique tiles
    for i in range(6):
        all_tiles.append(get_unique_tile_orientations(tiles[i]))

    for l in lines[30:]:
        size, tile_counts = l.split(": ")
        size = list(map(int, size.split("x")))
        tile_counts = list(map(int, tile_counts.split()))
        board = [[0 for _ in range(size[0])] for _ in range(size[1])]
        # visited = set()
        # start_counts = tile_counts.copy()

        def tile_fits(i, j, tile): # top left coord, pretty sure works
            for k in range(3):
                for l in range(3):
                    if (i+k < 0 or
                        j+l < 0 or
                        i+k >= len(board) or 
                        j+l >= len(board[0])):
                        return False
                    elif board[i+k][j+l] and tile[k][l]:
                        return False
            return True
        
        def tile_place(i, j, tile, tid):
            for k in range(3):
                for l in range(3):
                    if tile[k][l]:
                        board[i+k][j+l] = 1
            tile_counts[tid] -= 1
        
        def tile_remove(i, j, tile, tid):
            for k in range(3):
                for l in range(3):
                    if tile[k][l]:
                        board[i+k][j+l] = 0
            tile_counts[tid] += 1
        
        def backtrack(visited):
            if sum(tile_counts) == 0:
                return True
            flag = False
            i, j = -1, -1
            for k in range(len(board)):
                for l in range(len(board[0])):
                    if (k, l) not in visited:
                        i, j = k, l
                        flag = True
                        break
                if flag:
                    break
            if i == -1 and j == -1:
                return False

            visited.add((i, j))

            for tid, t_list in enumerate(all_tiles):
                if tile_counts[tid] == 0:
                    continue
                for t in t_list:
                    if tile_fits(i - 1, j - 1, t):
                        tile_place(i - 1, j - 1, t, tid)
                        # for k in range(len(board)):
                        #     for l in range(len(board[0])):
                        #         if board[k][l] == 0:
                        #             if backtrack(k, l):
                        #                 return True
                        # for mult in range(1, 3):
                        #     for dr, dc in DIRECTIONS:
                        #         dr *= mult
                        #         dr *= mult
                        #         if backtrack(i + dr, j + dc):
                        #             return True
                        if backtrack():
                            return True
                        tile_remove(i - 1, j - 1, t, tid)
            
            # if backtrack():
            #     return True

            visited.remove((i, j))
           
            # if tile_counts != start_counts:
            #     visited.remove((i, j))
            # else:
            #     backtrack()

            return False
        
        print(backtrack())
            
