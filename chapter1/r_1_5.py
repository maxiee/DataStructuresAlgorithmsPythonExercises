
def sum_n(n):
    return sum_n(range(1, n))

if __name__ == '__main__':
    #test1
    print('n=100, result:', sum_n(100))
    #test2
    print('n=1, result:', sum_n(1))
