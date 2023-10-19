import rabin_karp as horizontal
import vertical_check as vertical

file1000 = open("1000_pattern.txt", "r")
data1000 = file1000.read().splitlines()

file2000 = open("2000_pattern.txt", "r")
data2000 = file2000.read().splitlines()

file3000 = open("3000_pattern.txt", "r")
data3000 = file3000.read().splitlines()

file4000 = open("4000_pattern.txt", "r")
data4000 = file4000.read().splitlines()

file5000 = open("5000_pattern.txt", "r")
data5000 = file5000.read().splitlines()

file8000 = open("8000_pattern.txt", "r")
data8000 = file8000.read().splitlines()



pattern = ["A", "B", "C"]
potential_patterns = []
result = []
for line in data1000:
    potential_patterns.append(horizontal.rabin_karp(line, pattern))

for line in range(len(potential_patterns)-3):
    for index in potential_patterns[line]:
        if vertical.check(data1000, pattern, line, index):
            result.append([line,index])

print(result)
