#U2A1 - Simple Calculator
#This calculator will perform simple addition, subtraction, division, and multiplication

#Add a Header and calculator instructions
print("\t\t\tThis is a simple calculator\n")
print("Instructions:\n\tEnter your first number then press enter")
print("\tNext, enter your second number and press enter")
print("\tLastly, select an operator then press enter.\n")

#Catch any errors from the data input
try:
    #User inputs what the data they want calculated
    fnumber = int(input("Enter your first number "))
    snumber = int(input("Enter your second number "))
    
    #User chooses the operator
    op = input("Choose an operator. (+, -, /, *) ")

    #Process computation and print out user input
    if op == "+":
        print(fnumber + snumber)
    elif op == "-":
        print(fnumber - snumber)
    elif op == "/":
        print(fnumber / snumber)
    elif op == "*":
        print(fnumber*snumber)    
    else:
        print("Invalid entry")
#Add an excption error statement about error 
except ValueError:
    print("Invalid entry")






    