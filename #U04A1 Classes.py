#U04A1 Classes
#Created by Chris Misch
#This program will create a class to reverse a string word-by-word
#using two methods: 

#Class with 2 methods getString and printString
class Strings:
#Use __init__ to take resulting object along with class 
# constructors object and create an empty variable
    def __init__(self):
        self.string = ""
#create method that prompts user to enter a string
    def getString(self):
        self.string = input(f'Enter a string: ')
#Create a method that changes user's input into all uppercase
# and then prints out the result
    def printString(self):
#Using .upper() the method will change the inputed string to all uppercase
        print(self.string.upper())

#Set variable to the class then run getString method 
# and printString method
myObject = Strings()
myObject.getString()
myObject.printString()
