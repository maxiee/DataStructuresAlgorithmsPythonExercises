__author__ = 'maxiee'

def norm(v, p=2):
    sum = 0
    for i in v:
        sum += i ** p
    return sum ** (1.0 / p)

if __name__ == '__main__':
    print(norm([4,3]))
    print(norm([4,3,2,1], 3))