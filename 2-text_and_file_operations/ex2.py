import csv
import time as t

def read_data(path):
    result = []
    with open(path, "r") as file:
        data = csv.reader(file)
        for line in data:
            row = []
            if line[1] != "":
                row.append(line[0])
                row.append([])
                quote = ""
                for part in range(1, len(line)):
                    quote += line[part]
                row[1] = quote
                result.append(row)

    result.pop(0)
    return result

def sort_data(data):
    for row in data:
        row[0] = int(row[0])
    data.sort()

    for x in range(1, len(data)):
        if data[x][0] <= data[x-1][0]:
            data[x][0] = data[x-1][0] + 1

    return data

def swap_letter_case(data):
    for row in data:
        row[1] = row[1].lower()
    
    return data

def remove_by_prefix(data):
    for i in range(len(data)):
        quote = data[i][1].split()
        
        for word in quote:
            if len(word) > 1:
                if ord(word[0]) - ord(word[1]) == (1 or -1):
                    quote.remove(word)
                    data[i][1] = quote

                    
    return data



if __name__ == "__main__":

    quotes = read_data("data.csv")
    sorted_quotes = sort_data(quotes)
    lower_quotes = swap_letter_case(sorted_quotes)
    modified_quotes = remove_by_prefix(lower_quotes)

    for quote in modified_quotes:
        print(quote)
        t.sleep(1)
