__author__ = 'maxiee'

def all_different(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return False
    return True

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    if all_different(a):
        print("All the numbers are different!")
    else:
        print("There are some numbers be the same!")

    b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,5]
    if all_different(b):
        print("all the numbers are different!")
    else:
        print("There are some numbers be the same!")