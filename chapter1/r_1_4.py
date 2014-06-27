 
def sum_n(n):
    sum = 0
    for i in range(1, n):
        sum += i
    return sum

if __name__ == '__main__':
    #test1
    print('n=100, result:', sum_n(100))
    #test2
    print('n=1, result:', sum_n(1))