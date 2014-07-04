__author__ = 'maxiee'

if __name__ == '__main__':
    a = [1, 2, 3]
    try:
        a[4] = 233
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")