__author__ = 'maxiee'

def factors(n):
    k = 1
    temp = []
    while k * k < n:
        if n % k == 0:
            yield k
            temp.insert(0, n // k)
        k += 1
    if k * k == n:  # divides evenly, thus k is a factor
        yield k
    for i in temp:
        yield i

if __name__ == '__main__':
    for factor in factors(100):
        print(factor)