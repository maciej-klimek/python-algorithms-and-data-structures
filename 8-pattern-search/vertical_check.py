def check(sequence, pattern, y, x):
    for letter in pattern:
        if sequence[y][x] != letter:
            return False
        else:
            y += 1
    return True


if __name__ == "__main__":
    table = [
        [
            "G",
            "F",
            "I",
            "A",
            "B",
            "C",
            "E",
            "R",
            "S",
            "W",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "H",
            "T",
            "U",
        ],
        [
            "B",
            "X",
            "V",
            "D",
            "Y",
            "Z",
            "C",
            "U",
            "L",
            "R",
            "S",
            "A",
            "N",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
        ],
        [
            "C",
            "M",
            "N",
            "W",
            "A",
            "B",
            "C",
            "Q",
            "P",
            "O",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
        ],
        [
            "I",
            "J",
            "K",
            "L",
            "B",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "A",
            "B",
        ],
        [
            "X",
            "Y",
            "Z",
            "B",
            "C",
            "A",
            "E",
            "D",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "A",
            "B",
            "C",
        ],
        [
            "B",
            "C",
            "A",
            "D",
            "X",
            "Y",
            "Z",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
        ],
        [
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "A",
            "B",
            "C",
            "D",
            "X",
            "Y",
            "Z",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
        ],
        [
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
        ],
        [
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
        ],
        [
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "A",
            "B",
            "C",
            "D",
            "E",
        ],
        [
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
        ],
        [
            "X",
            "Y",
            "Z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "A",
            "C",
            "L",
            "M",
            "N",
        ],
    ]

    for line in range(len(table) - 2):
        for letter in range(20):
            print(check(table, ["A", "B", "C"], line, letter))