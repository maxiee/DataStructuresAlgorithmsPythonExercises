
def my_reverse(data):
    for i in range(int(len(data)/2)):
        temp = data[i]
        data[i] = data[-1*(i+1)]
        data[-1*(i+1)] = temp
    return data

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    print('test:', my_reverse(a))