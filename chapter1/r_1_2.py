
# if k is even, return True
# else return False
def even(k):
    return str(k)[-1] in ('0', '2', '4', '6', '8')

if __name__ == '__main__':
    #test1
    print('k = 4')
    print(even(4))
    #test2
    print('k = 5')
    print(even(5))
