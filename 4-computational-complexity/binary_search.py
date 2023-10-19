def binary_search(start, end, target, tbl):
    mid = (start+end)//2
    if tbl[mid] == target:
        return mid
    else:
        if tbl[mid] > target:
            return binary_search(start, mid-1, target, tbl)
        else:
            return binary_search(mid+1, end, target, tbl)
        
        



def main():
    A = [1, 3, 5, 7, 9, 10, 45, 60, 77, 123, 145]
    print(f"Znaleziono element na indeksie {binary_search(0, len(A)-1, 9, A)}")

main()