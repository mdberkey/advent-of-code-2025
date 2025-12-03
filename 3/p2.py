
with open("input") as f:
    res = 0

    for line in f:
        line = line.strip()
        line = [int(num) for num in line]

        def get_max_and_ind(i, j): #inc, ex
            curr_max = line[i]
            curr_ind = i

            for k in range(i, j):
                if line[k] > curr_max:
                    curr_max = line[k]
                    curr_ind = k
            
            return curr_max, curr_ind + 1

        joltage = []
        curr_ind = 0
        for i in range(11, -1, -1):
            curr_val, curr_ind = get_max_and_ind(curr_ind, len(line) - i)
            joltage.append(str(curr_val))

        val = int("".join(joltage))
        print(val)
        res += val

    print(res)
