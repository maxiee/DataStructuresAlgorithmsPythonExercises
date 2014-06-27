
def sum_n_odd(n):
    sum = 0
    for i in range(1, n, 2):
        sum += i
    return sum

if __name__ == '__main__':
    #test1
    print('n=5, result:', sum_n_odd(5))
    #test2
    print('n=10, result:', sum_n_odd(10))
