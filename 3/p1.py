import math

with open("input") as f:
    res = 0

    for line in f:
        line = line.strip()
        nums = [int(num) for num in line]
        max_num = max(nums[:-1])
        next_max_num = -math.inf
        seen_max = False

        for num in nums:
            if not seen_max and num == max_num:
                seen_max = True
            elif seen_max:
                next_max_num = max(next_max_num, num)
        
        res += 10 * max_num + next_max_num

    print(res)