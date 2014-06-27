
def minmax(data):
    min = data[0]
    max = data[0]
    for i in data:
        if min < i:
            min = i
        if max > i:
            max = i
    return (min, max)

if __name__ == '__main__':
    #test1
    list1 = [40, 98, 11, 27, 100, 50, 4]
    print("The list is:",list1)
    min, max = minmax(list1)
    print('min is:', min, '\nmax is:', max)
