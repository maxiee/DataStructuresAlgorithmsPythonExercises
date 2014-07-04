__author__ = 'maxiee'

# parameter position is used for read_line_reverse
def read_line(fp, position):
    tail = fp.seek(0, 2)
    fp.seek(0, 0)
    position.append(fp.tell())
    while True:
        str = fp.readline().strip('\n')
        print(str)
        if fp.tell() >= tail:
            break
        position.append(fp.tell())


# parameter position must be used in read_line FIRST!
def read_line_reverse(fp, position):
    for i in range(1, len(position)+1):
        fp.seek(position[-i])
        print(fp.readline().strip('\n'))

if __name__ == '__main__':
    fp = open('test.txt')
    position = []
    read_line(fp, position)
    print(position)
    read_line_reverse(fp, position)