__author__ = 'maxiee'

if __name__ == '__main__':
    a = [i for i in range(10)]
    b = [i for i in range(10, 20)]
    c = [a[i]*b[i] for i in range(10)]
    print(a)
    print(b)
    print(c)