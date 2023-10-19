def check(pattern, sequence):
    result = []
    for line in range(len(sequence) - 2):
        for i in range(len(sequence[line]) - 2):
            if (
                sequence[line][i] == pattern[0]
                and sequence[line][i + 1] == pattern[1]
                and sequence[line][i + 2] == pattern[2]
            ):
                if (
                    sequence[line + 1][i] == pattern[1]
                    and sequence[line + 2][i] == pattern[2]
                ):
                    result.append([line, i])
    return result


pattern = ["A", "B", "C"]
main_file = open("1000_pattern.txt", "r")
data = main_file.read().splitlines()
