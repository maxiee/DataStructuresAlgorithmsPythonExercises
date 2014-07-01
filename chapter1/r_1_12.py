import random

def my_choice(data):
    return data[random.randrange(len(data))]

if __name__ == '__main__':
    a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
    for i in range(10):
        print('test',i,":",my_choice(a))