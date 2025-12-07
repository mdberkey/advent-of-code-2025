
with open("input") as f:
    lines = [line.strip("\n") for line in f]
    max_row = max([len(row) for row in lines])

    for i, row in enumerate(lines):
        lines[i] += " " * (max_row - len(row))
    
    nums, ops = lines[:-1], lines[-1]

    op_cols = []
    op_i = -1
    vals = []
    curr_op = ops[0]

    for char in ops:
        if char != " ":
            curr_op = char
            op_i += 1
            vals.append(1) if curr_op == "*" else vals.append(0)
        op_cols.append((curr_op, op_i))

    for j in range(len(nums[0]) - 1, -1, -1):
        curr_num = 0
        for i in range(len(nums)):
            if nums[i][j] != " ":
                curr_num *= 10
                curr_num += int(nums[i][j])

        if curr_num != 0:
            op, val_i = op_cols[j]
            if op == "*":
                vals[val_i] *= curr_num
            else:
                vals[val_i] += curr_num
    
    print(sum(vals))
