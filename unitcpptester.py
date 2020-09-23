import subprocess
import sys
import os
import time

def returnLines(inputFilePath): #returns an array with all arguements of a file
    with open(inputFilePath) as reader:
        #read and store the lines from the file
        inputFileLines = reader.readlines()
        return inputFileLines #syntax for line is inputFileLines[n-1] where n is the desired line number

def getInputFile(): #gets the path of the input file
    print(sys.argv)
    if len(sys.argv) != 2:
        sys.exit("include the path to the input file as the only argument")
    return sys.argv[1]


def runCpp(filePath, input): #runs the CPP comment
    data, temp = os.pipe()
    os.write(temp, bytes(input, "utf-8"))
    os.close(temp)
    s = subprocess.check_output(filePath, stdin = data, shell=True)
    return s.decode("utf-8")

#/***********MAIN CODE**************/

inputFilePath = getInputFile() #input file for test cases & commands
lines = returnLines(inputFilePath)
command = lines[0]
lines = lines[1:]
outputWriter = open("output.txt", "w")

for line in lines:
    output = runCpp(command, line)
    outputWriter.write(line)
    outputWriter.write(output)
    outputWriter.write("\n \n")

outputWriter.close()

#linux and mac is ./test or path to compiled file
#windows is 'start test.exe'
# start C:/s/s/cdcd/ds/csd/test.exe
# /s/s/sc/sdcsd/sdv/ssdfg/test

