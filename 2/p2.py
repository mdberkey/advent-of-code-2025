
def is_id_invalid(id):
    id_str = str(id)
    seq_len = len(id_str) // 2

    while seq_len > 0:
        if len(id_str) % seq_len != 0:
            seq_len -= 1
            continue
        
        left_str = id_str[:seq_len]
        invalid = True
        for i in range(seq_len, len(id_str), seq_len):
            if id_str[i:i+seq_len] != left_str:
                invalid = False
                break
        
        if invalid:
            return True

        seq_len -= 1
    
    return False
        
with open("input") as f:
    res = 0

    for line in f:
        ranges = line.strip().split(",")
        for ran in ranges:
            l, r = ran.split("-")
            for id in range(int(l), int(r) + 1):
                if is_id_invalid(id):
                    res += id
    
    print(res)
