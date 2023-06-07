
def create_string():
    result = ''
    for num in range(500, 3000):
        if num % 7 == 0 and num % 5 != 0:
            result += str(num)

    return result

def change_21_to_XX(num_string):
    
    count = 0
    tbl = list(num_string)
    for i in range(len(tbl)):
        if tbl[i] == '2':
            if tbl[i+1] == '1':
                count += 1
                tbl[i], tbl[i+1]  = "X", "X"
        
    print(f"'21' occurs {count} times.")
    print("".join(tbl))


if __name__ == "__main__":
    num_string = create_string()
    change_21_to_XX(num_string)

