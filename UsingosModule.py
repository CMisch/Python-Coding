#Practicewithosmodule.py
#Lessons derived from book Learn to Program with Python (Apress 2016)

#Functions for checking if a file exists, read from a file, write to a file

import os
#This method allows you to use an easier path to see if a file exists
# instead of having to write a lenghtier os.path.exist() method
def fileExists(filePath):
    exits = os.path.exists(filePath)
    return exits

#This method will rewrite a file with a new string you give it by adding the filepath
# and then adding what you want to overwrite it with
def writeFile(filePath, testToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(testToWrite)
    fileHandle.close()

#This method will check to see if a file exists then read it to you
# and if the file does not exist it will tell you it does not exist
def readFile(filePath):
    if not fileExists(filePath):
        print('The file, ' + filePath + 'does not exist -cannot read it')
        return ""
    else:
        fileHandle = open(filePath, 'r')
        data = fileHandle.read()
        fileHandle.close()
    return data



#Program to test methods 
#file_path = 'textTestFilez.txt' #Setting a variable to the file location
#
#stringToWriteFile = 'This is my test file... that I am creating \nusing os module and in-house methods'
#writeFile(file_path, stringToWriteFile)
#
#viewFile = readFile(file_path)
#
#print('Read-in:', viewFile)
