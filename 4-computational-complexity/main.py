import random as r
import time as t

def generate(a, b, l):
    tbl = []
    for i in range(l):
        tbl.append(r.randint(a, b))
    return tbl

def insert_sort(tbl):
    for i in range(1, len(tbl)):
        x = tbl[i]
        j = i - 1
        while j >= 0 and tbl[j] > x:
            tbl[j+1] = tbl[j]
            j = j -1
        tbl[j+1] = x


def merge(mainTbl, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mainTbl[k] = left[i]
            i += 1
        else:
            mainTbl[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        mainTbl[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        mainTbl[k]=right[j]
        j += 1
        k += 1


def merge_sort(tbl):
    if len(tbl) > 1:
        mid = len(tbl)//2
        l = tbl[:mid]
        r = tbl[mid:]

        merge_sort(l)
        merge_sort(r)
        merge(tbl, l, r)

def main():

    insert_times = []
    merge_times = []
    range_start = 0
    range_end = 100
    count = 200
    length = 2000


    for i in range(count):
        start = t.time()
        insert_sort(generate(range_start, range_end, length))
        end = t.time()
        insert_times.append(end-start)

        start = t.time()
        merge_sort(generate(range_start, range_end, length))
        end = t.time()
        merge_times.append(end-start)
        

    print(f"Najgorszy czas dla insertion sort -> {max(insert_times)}")
    print(f"Najlepszy czas dla insertion sort -> {min(insert_times)}")
    print(f"Średni czas dla insertion sort -> {sum(insert_times)/len(insert_times)}")
    print()
    print(f"Najgorszy czas dla merge sort -> {max(merge_times)}")
    print(f"Najlepszy czas dla merge sort -> {min(merge_times)}")
    print(f"Średni czas dla merge sort -> {sum(merge_times)/len(merge_times)}")
         

main()