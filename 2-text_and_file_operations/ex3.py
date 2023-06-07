import time

#plik SJP.txt był za duży więc wysłałem bez

def read_data():
    f = open("SJP.txt", "r")
    data = f.read()
    word_list = data.splitlines()

    return word_list


def sort_two_dim(words):
    sorted_words = []
    sorted_words.append([words[0]])

    ind = 0
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][0]:
            ind+=1
            sorted_words.append([words[i]])
        else:
            sorted_words[ind].append(words[i])
    return sorted_words

def check_if_in_SJP(words):
    word = str(input("Podaj slowo: "))
    word = word.lower()
    start = time.time()
    for letter in words:
        if word in letter:
            print("Twoje slowo jest w SJP")
            print(time.time() - start)
            return True
    print("Twojego slowa nie ma w SJP")
    return False
        

def main():

    word_list = read_data()
    sorted_words = sort_two_dim(word_list)
    check_if_in_SJP(sorted_words)

main()






