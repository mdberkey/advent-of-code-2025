def is_id_invalid(id):
    id_str = str(id)
    if len(id_str) % 2 == 1:
        return False

    l = 0
    r = len(id_str) // 2
    while r < len(id_str) and id_str[l] == id_str[r]:
        l += 1
        r += 1
    
    return r == len(id_str)


with open("input") as f:
    
    res = 0

    for line in f:
        ranges = line.strip().split(",")
        for ran in ranges:
            l, r = ran.split("-")
            l_int, r_int = int(l), int(r)
            for id in range(l_int, r_int + 1):
                if is_id_invalid(id):
                    res += id
    
    print(res)