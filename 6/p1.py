
with open("input") as f:
    res = 0

    lines = [line.strip() for line in f]
    
    nums, ops = lines[:-1], lines[-1]
    ops = ops.split()
    
    vals = [1 if op == "*" else 0 for op in ops]
    for num_list in nums:
        for i, num in enumerate(num_list.split()):
            if ops[i] == "*":
                vals[i] *= int(num)
            else:
                vals[i] += int(num)
    
    print(sum(vals))
