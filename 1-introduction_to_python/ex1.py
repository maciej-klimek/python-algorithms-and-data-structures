

def create_list(tbl):
    i = 0

    while len(tbl) < 48:
        x =  (tbl[i] + tbl[i+1])/(tbl[i+1] - tbl[i])
        tbl.append(x)
        i+=1

    return tbl

def get_average_and_mode(tbl):
    sum = 0
    for num in tbl:
        sum+=num

    print(f"Average value = {sum/48}")

    index_tbl = [0]*48
    
    for i in range(len(tbl)-1):
        for j in range(i, len(tbl)-1):
            if tbl[i] == tbl[j]:
                index_tbl[i]+=1

    mode = index_tbl.index(max(index_tbl))

    if tbl[mode] == 1:
        print("List has no mode, each value occurs only once")
    else:
        print(f"Mode = {tbl[mode]}")

if __name__ == "__main__":
    L = create_list([1, 2])
    get_average_and_mode(L)

