#Create a calculator UI


from tkinter import *

root = Tk()
root.title("My Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
#create a grid that spans over 3 columns
e.grid(row=0, column=0,columnspan=3, padx=10, pady=10)
#define buttons
def button_click(number):
    current = e.get()                       #sets variable current to e.get() to grab user input
    e.delete(0,END)                         #by deleting last entry prevents previous input to be displayed
    e.insert(0, str(current) + str(number)) #contatinates current and number as a string 

def  button_clearing():
    e.delete(0, END)
#first_number = 0            #prevents variable used in def to be empty

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equals():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    
#create methods that define what each button does
def button_sub():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)
    
def button_div():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)
    
def button_x():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

    
#add buttons: using lambda allows you to pass input 
button1 =Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 =Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 =Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 =Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 =Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 =Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 =Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 =Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 =Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 =Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_ad = Button(root, text="+", padx=39, pady=20, command= button_add)       #remember to remove () for function when using command
button_equal = Button(root, text="=", padx=89.8, pady=20, command= button_equals)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clearing)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_sub)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_div)
button_multiply=Button(root, text="*", padx=40, pady=20, command=button_x)

#put buttons on screen
button1.grid(row= 3, column= 0)
button2.grid(row= 3, column= 1)
button3.grid(row= 3, column= 2)

button4.grid(row= 2, column= 0)
button5.grid(row= 2, column= 1)
button6.grid(row= 2, column= 2)

button7.grid(row= 1, column= 0)
button8.grid(row= 1, column= 1)
button9.grid(row= 1, column= 2)

button0.grid(row= 4, column= 0)
button_clear.grid(row= 4, column= 1, columnspan= 2)
button_ad.grid(row= 5, column= 0)
button_equal.grid(row= 5, column= 1, columnspan= 2)

button_subtract.grid(row= 6, column= 0)
button_divide.grid(row=6, column=2)
button_multiply.grid(row=6, column=1)

root.mainloop()