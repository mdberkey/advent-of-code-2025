
def is_id_invalid(id_str):
    if len(id_str) % 2 == 1:
        return False

    curr = seq_size = len(id_str) // 2
    while curr < len(id_str) and id_str[curr] == id_str[curr - seq_size]:
        curr += 1
    
    return curr == len(id_str)

with open("input") as f:
    res = 0

    for line in f:
        ranges = line.strip().split(",")
        for ran in ranges:
            l, r = ran.split("-")
            for id in range(int(l), int(r) + 1):
                if is_id_invalid(str(id)):
                    res += id
    
    print(res)
