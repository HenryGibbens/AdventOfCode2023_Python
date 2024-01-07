import os

#1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#trb7uchet
#In this example, the calibration values of these four lines are
# 12, 38, 15, and 77. Adding these together produces 142.

# find first occurence of any number string in line
def firstNumber(line):

    lowestFoundIndex = len(line)
    lowestFoundNumber = ""
    lowestFoundNumberVal = 0

    if False:
        iZ = line.find("zero") # 3
        # is iz the smallest positive integer found so far?
        if iZ > -1 and iZ < lowestFoundIndex:
            lowestFoundIndex = iZ
            lowestFoundNumber = "zero"

        iO = line.find("one")
        if iO > -1 and iO < lowestFoundIndex:
            lowestFoundIndex = iO
            lowestFoundNumber = "one"

    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    y = 0
    for x in numbers:
        iO = line.find(x)
        if iO > -1 and iO < lowestFoundIndex:
            lowestFoundIndex = iO
            lowestFoundNumber = x
            lowestFoundNumberVal = y
        y = y + 1
    #print("{} = {},{}".format(line,lowestFoundNumber,lowestFoundNumberVal))
    return lowestFoundNumber,lowestFoundNumberVal

def oldProcessLineOfInputIntoStruct(line, struct):
    #print(line)
    copyLine = line
    #line = line.lower()
    toReplace,replaceWith = firstNumber(line)
    while replaceWith > 0:
      line = line.replace(toReplace,str(replaceWith)+toReplace[-1])
      toReplace,replaceWith = firstNumber(line)
    # following code finds the first and last digits and adds them
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
    print("{} = {} = {}".format(copyLine.rstrip(),line.rstrip(),firstDigit+secondDigit))

def processLineOfInputIntoStruct(line, struct):

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game =line.split(":")
    gameID =  int(game[0].split(" ")[1])
    draws = game[1].split(";")
    print(game[0],draws) # returns ['Game 1', ' 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']

    maxDrawnRed = 0
    maxDrawnGreen = 0
    maxDrawnBlue = 0

    for draw in draws:
        colours = draw.split(",")
        #print(colours)
        for colour in colours:
            print(colour.strip().split(" "))
            numcol = colour.strip().split(" ")
            if numcol[1] == "red":
                num = int(numcol[0])
                if num > maxDrawnRed:
                    maxDrawnRed = num
            if numcol[1] == "green":
                num = int(numcol[0])
                if num > maxDrawnGreen:
                    maxDrawnGreen = num
            if numcol[1] == "blue":
                num = int(numcol[0])
                if num > maxDrawnBlue:
                    maxDrawnBlue = num
    # for this game what is the largest number of red cubes drawn?

    # for this game what is the largest number of green cubes drawn?
    # for this game what is the largest number of blue cubes drawn?
    maxReds = 12
    maxGreen = 13
    maxBlue = 14
    gamePossible = True

    if maxDrawnRed > maxReds :
        gamePossible = False

    if maxDrawnGreen > maxGreen :
        gamePossible = False

    if maxDrawnBlue > maxBlue :
        gamePossible = False


    if gamePossible:
        struct.append(gameID)

def processInputFile(filePath):
    struct = []
    if os.path.exists(filePath):
        f = open(filePath, "r")

        yz = 0
        for x in f:
            processLineOfInputIntoStruct(x, struct)
            yz = yz + 1

    return struct

def processStruct(struct):
    # add values one at a time to total
    total= 0
    for value in struct:
        print(value)
        total = total + value
    print(total)



def mainTask():
    input_path = "/home/pi/git/AdventOfCode2023_Python/02a/ full.input.txt"
    struct = processInputFile(input_path)
    processStruct(struct)
    #firstNumber("one")
    #firstNumber("zero")
    #firstNumber("two")
    ##firstNumber("onezero")
    #firstNumber("zerone")
    #firstNumber("zeroone")
    #firstNumber("twone")
    #firstNumber("onetwo")
    #firstNumber("zerotwo")
    #firstNumber("twozero")
if __name__ == "__main__":
    mainTask()