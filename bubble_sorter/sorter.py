import os
from random import randint

# ta realná sort funcke
def bubble_sort(sort_in):
    for _ in range(len(sort_in)):
        for i in range(len(sort_in) - 1):
            if sort_in[i] > sort_in[i + 1]:
                sort_in.insert(i + 1, sort_in.pop(i))
    return sort_in

# tester toho jestli ta moje funkce funguje (zkouší to na základně .sort())
def test_sort():
    vzorek = []
    for _ in range(100):
        vzorek.append(randint(0, 100))
    out = bubble_sort(vzorek)
    vzorek.sort()
    if out != vzorek:
        print("neprošel \n", out, vzorek, "\n-----------------------------")
    else:
        print("prošel")

#for _ in range(100):
#    test_sort()

# vytváří soubory s náhodně zamíchanými čísly
def create_files(path, count, num_count):
    for i in range(count):
        file = open(path + "/" + str(i) + ".txt", "w")
        file.write(",".join(list(map(lambda x: str(randint(0, 100)), [""] * num_count))))
        file.close()


# nachází soubory a seřazuje v nich náhodně zamíchané čísla, načeš soubor upravý s objektivně lepšími změnami
def find_files(path):
    for file_nam in os.listdir(path):
        file = open(path + "/" + file_nam)
        print(file_nam, "- sorted:", bubble_sort(list(map(lambda x: int(x), file.read().split(",")))), "\n\n")
        file.close()

if __name__ == "__main__":
    create_files(os.getcwd() + "/files", 1000, 200)
    find_files(os.getcwd() + "/files")
