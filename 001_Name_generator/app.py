import string
import random as rd

letters = string.ascii_lowercase
let = len(letters)

def nameGenerator(number_of_names, min_len = 5, max_len = 10):
    """This function returns list of random names"""
    names = []
    for i in range(0, number_of_names):
        name = ""
        for i in range(0, rd.randint(min_len, max_len+1)):
            name += letters[rd.randint(0,let-1)]
        names.append(name.title())
    return names


print(nameGenerator(12, 4, 15))

