__author__ = 'maxiee'

def formula_test(a,b,c):
    if a + b == c:
        print("%d + %d = %d" %(a,b,c))
        return
    elif a == b - c:
        print("%d = %d -%d" %(a,b,c))
    elif a * b == c:
        print("%d * %d = %d" %(a,b,c))
    else:
        print("unknown formula!")

if __name__ == '__main__':
    formula_test(1,2,3)
    formula_test(1,3,2)
    formula_test(2,5,10)
    formula_test(9,9,0)
    formula_test(0,1,1000)