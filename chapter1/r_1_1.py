
# for example, i = 27
def is_multiple(n,m):
    return n == m * 27

if __name__ == '__main__':
    # test1
    print('n=27,m=1:')
    print(is_multiple(27, 1))
    # test2
    print('n=28,m=1:')
    print(is_multiple(28, 1))
    # test3
    print('n=270,m=10:')
    print(is_multiple(270, 10))