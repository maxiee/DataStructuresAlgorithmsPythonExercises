__author__ = 'maxiee'
import string

def remove_punc(str):
    ret = ""
    for i in str:
        if i not in string.punctuation:
            ret += i
    return ret

if __name__ == '__main__':
    sentence = "Let's try, Mike."
    print("sentence:", sentence)
    print("remove_punc:", remove_punc(sentence))