import os

#1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet
#In this example, the calibration values of these four lines are
# 12, 38, 15, and 77. Adding these together produces 142.


def processLineOfInputIntoStruct(line, struct):
    #print(line[0].isdigit())
    foundFirstDigit = False
    firstDigit = -1
    secondDigit = -1
    for char in line:
       # print(char.isdigit())
        if char.isdigit():
            if not foundFirstDigit:
              firstDigit = int(char)*10
              foundFirstDigit = True
            secondDigit = int(char)
    # process one line
    # find first digit
    #use if statement to see if its a digit
    # find last digit
    # first * 10 + second
    # put number into struct
    struct.append(firstDigit+secondDigit)

def processInputFile(filePath):
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")
        for x in f:
            processLineOfInputIntoStruct(x, struct)
    return struct

def processStruct(struct):
    # add values one at a time to total
    total = 0
    for value in struct:
        print(value)
        total = total + value
    print(total)

def mainTask():
    input_path = "/home/pi/git/AdventOfCode2023_Python/01a/input.txt"
    struct = processInputFile(input_path)
    processStruct(struct)

if __name__ == "__main__":
    mainTask()