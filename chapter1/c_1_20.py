__author__ = 'maxiee'
import random

def my_shuffle(data):
    temp = [None] * len(data)
    for i in data:
        index = random.randint(0,len(data)-1)
        while temp[index] != None:
            index = random.randint(0,len(data)-1)
        temp[index] = i
    return temp

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    print(a)
    b = my_shuffle(a)
    print(b)