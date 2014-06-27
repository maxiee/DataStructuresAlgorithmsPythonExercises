
def gen_list():
    list = []
    for i in range(9):
        list.append(2**i)
    return list

if __name__ == '__main__':
    print(gen_list())