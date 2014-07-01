__author__ = 'maxiee'

def scale(data, factor):
    for val in data:
        val *= factor

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    scale(a, 5)
    print(a)

# it doesn't work properly, the values of a hasn't changed.
# because from line 5:
#   val *= factor
# val is a temporary variable. this line only updates the reference of val
# the reference of a hasn't changed (updated).