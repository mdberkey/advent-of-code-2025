
with open("input") as f:
    lines = [line.strip() for line in f]
    nums, ops = lines[:-1], lines[-1].split()
    vals = [1 if op == "*" else 0 for op in ops]

    for num_str in nums:
        for i, num in enumerate(num_str.split()):
            if ops[i] == "*":
                vals[i] *= int(num)
            else:
                vals[i] += int(num)
    
    print(sum(vals))
