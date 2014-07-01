__author__ = 'maxiee'

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    scale(a, 5)
    print(a)

# the result of print(a) is:
#   [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
# from line 8:
#   a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# List a keeps the reference to its elements
# from line 5:
#   data[j] *= factor
# the *= operator causes the creation of a new instance
# then a updates its reference to this new instance
# so when the loop finished, a keeps all the latest references
