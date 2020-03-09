import sys 
import numpy as np
import math as m

charMap = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
key_list = list(charMap.keys()) 
val_list = list(charMap.values()) 



def write_to_OutputFile(text, file):
    f = open(file, "a")
    f.write(text)
    f.close()


def shift(operation, input_file, output_file, Key):
    file = open(output_file, "w")
    file.truncate()
    file.close()
    key = int(Key)
    print(output_file)
    if operation == 'enc' or operation == 'encrypt':
        f = open(input_file, "r")
        plaintext = f.read().upper() 
        words = plaintext.split()
        for word in words:
            cipherStream=[]
            plainStream = split(word)
            for char in plainStream:
                plainStream = split(plaintext)
                value = charMap[char]
                cipher = np.mod((int(value) + key), 26)
                cipherStream.append(cipher)
            cipherText=''
            for value in cipherStream:
                char = key_list[val_list.index(value)]
                cipherText += char
            cipherText +='  '
            write_to_OutputFile(cipherText, output_file)

    elif operation == 'dec' or operation == 'decrypt' :
        plainStream =[]
        f = open(input_file, "r")
        cipherText = f.read().upper()
        words = cipherText.split()
        for word in words:
            plainStream=[]
            cipherStream = split(word)
            additive_invers = 26 - key
            for char in cipherStream:
                value = charMap[char] 
                plain = np.mod((int(value) + additive_invers), 26)
                plainStream.append(plain)
            plaintext=''
            for value in plainStream:
                char = key_list[val_list.index(value)]
                plaintext += char
            plaintext+="  "
            write_to_OutputFile(plaintext, output_file) 

    

def MOD_INVERSE(a):
    if m.gcd( a, 26) != 1:
        print('error wrong key')
        return 
    else:
        a = a % 26
    for x in range(1, 26) : 
        if ((a * x) % 26 == 1) : 
            return x 
    


def affine(operation, input_file, output_file, a, b):
    file = open(output_file, "w")
    file.truncate()
    file.close()
    cipherStream=[]
    key = int(b)
    if operation == 'enc' or operation == 'encrypt':
        f = open(input_file, "r")
        plaintext = f.read().upper()
        words = plaintext.split()
        for word in words:
            cipherStream=[]
            plainStream = split(word)
            for char in plainStream:
                value = charMap[char]
                y = int(value) * int(a)
                cipher = np.mod((y + key), 26)
                cipherStream.append(cipher)
            cipherText=''
            for value in cipherStream:
                char = key_list[val_list.index(value)]
                cipherText += char
            cipherText+="  "
            write_to_OutputFile(cipherText, output_file)

    elif operation == 'dec' or operation == 'decrypt' :
        plainStream =[]
        f = open(input_file, "r")
        cipherText = f.read().upper()
        words = cipherText.split()
        for word in words:
            plainStream=[]
            cipherStream = split(word)
            additive_invers = 26 - key
            multi_invers = int(MOD_INVERSE(int(a)))
            for char in cipherStream:
                value = charMap[char] 
                y = multi_invers*(int(value) + additive_invers)
                plain = np.mod(y, 26)
                plainStream.append(plain)
            plaintext=''
            for value in plainStream:
                char = key_list[val_list.index(value)]
                plaintext += char
            plaintext+=" "
            write_to_OutputFile(plaintext, output_file)
        

def split(word): 
    return [char for char in word]  

        
def CRYPTO(cipher, operation, input_file, output_file, b, a=0):
    if cipher == 'shift':
        shift(operation, input_file, output_file, b)
    elif cipher == 'affine':
        affine(operation, input_file, output_file, b, a)





if __name__ == '__main__':
    args = len(sys.argv)
    if args == 6:
        CRYPTO(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif args == 7:
        CRYPTO(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    