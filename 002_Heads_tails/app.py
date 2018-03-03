import random as rd


def throw(number_of_throws=1):
    for i in range(0, number_of_throws):
        if round(rd.random()):
            print('Heads')
        else:
            print('Tails')


throw(10)
