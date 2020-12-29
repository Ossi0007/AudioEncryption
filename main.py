import time
import pyaudio
import os
import math
import wave
import codecs
import struct
import  random


def solvesud(c, n):
    rowIndex = -1
    colIndex = -1
    isEmpty = True
    for i in range(0, n):
        for j in range(0, n):
            if c[i][j] == 0:
                rowIndex = i
                colIndex = j
                isEmpty = False
                break
        if not isEmpty:
            break
    if isEmpty:
        return True
    else:
        for val in range(1, n + 1):
            if isSafe(c, val, rowIndex, colIndex, n):
                c[rowIndex][colIndex] = val
                if solvesud(c, n):
                    return True
                else:
                    c[rowIndex][colIndex] = 0
    return False


def isSafe(c, value, rowIndex, colIndex, n):
    # rowCheck
    for j in range(0, n):
        if c[rowIndex][j] == value:
            return False
    # colCheck
    for i in range(0, n):
        if c[i][colIndex] == value:
            return False
    # BoxCheck
    baseRowIndex = rowIndex - (rowIndex % boxLength)
    baseColIndex = colIndex - (colIndex % boxLength)

    for i in range(baseRowIndex, baseRowIndex + boxLength):
        for j in range(baseColIndex, baseColIndex + boxLength):
            if c[i][j] == value:
                return False
    return True


def getSum(n):
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)



if __name__ == '__main__':
    b =   [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    b[random.randrange(0,16)][random.randrange(0,16)]=random.randrange(1,17)
    n = len(b)
    boxLength = int(math.sqrt(n))

    if solvesud(b, n):
        for row in b:
            print(' '.join(map(str, row)))
    else:
        print("no solution")
# here we are using unix timestamp
    tStamp = math.trunc(time.time())
    print(tStamp)
    p = getSum(tStamp)
    print(p)
    t = p % 16
    u = p % 100




# Converting frames of wav file into its binary
    with open("filename_temporary.txt",'w') as fp:

        song = wave.open(r'C:\Users\0007\file_example_WAV_1MG.wav', 'rb')
        print(song.getparams())
        length = song.getnframes()
        values = []
        print(length)
        for x in range(length):
            string = song.readframes(1)
            i = struct.unpack('hh', string) #for
            # j = struct.unpack('<H',string)
            # i=struct.unpack('<h',string) for 8bitaudio
            # sample=(bin(i[0]),bin(i[1]))
            fp.write(bin(i[0])+" "+bin(i[1])+"\n")
