
def sum_n_odd(n):
    return sum(range(1, n, 2))

if __name__ == '__main__':
    #test1
    print('n=5, result:', sum_n_odd(5))
    #test2
    print('n=10, result:', sum_n_odd(10))
