__author__ = 'maxiee'

def product_odd_pairs(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if (data[i] * data[j]) %2 == 1:
                print('found a pair:', data[i], data[j])

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    product_odd_pairs(a)