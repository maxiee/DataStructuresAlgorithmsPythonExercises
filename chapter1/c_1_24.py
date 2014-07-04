__author__ = 'maxiee'

if __name__ == '__main__':
    fp = open('test.txt')
    tail = fp.seek(0, 2)
    fp.seek(0, 0)
    count = 0
    while True:
        char = fp.read(1)
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
        if fp.tell() == tail:
            break
    print(count)