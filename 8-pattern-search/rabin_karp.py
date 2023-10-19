def rabin_karp(sequence, pattern):
    result = []
    n = len(sequence)
    m = len(pattern)
    patternHash = get_hash_value(pattern)

    for i in range(n - m + 1):
        sliceHash = get_hash_value(sequence[i : i + m])
        if sliceHash == patternHash and check_slice(sequence, i, i + m - 1, pattern):
            result.append(i)

    return result

def get_hash_value(string):
    hashValue = 0
    for char in string:
        hashValue = hashValue + ord(char) - ord("A")
    return hashValue

def check_slice(sequence, start, end, pattern):
    for i in range(start, end + 1):
        if sequence[i] != pattern[i - start]:
            return False
    return True

if __name__ == "__main__":

    sequence = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C"]
    pattern = ["A", "B"]

    result = rabin_karp(sequence, pattern)
    print(result)
