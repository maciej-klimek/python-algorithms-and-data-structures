import time

tbl = []
for i in range(10000):
    tbl.append(i)

start1 = time.time()
for i in tbl:
    print(i, end=" ")
end1 = time.time()

print()

start2 = time.time()
for i in range(1000):
    print(tbl[i], end=" ")
end2= time.time()

print()

print(end1-start1, "vs", end2-start2)