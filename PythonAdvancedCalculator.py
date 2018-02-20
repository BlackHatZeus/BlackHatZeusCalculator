from tkinter import *

'#Defining The Window'

root = Tk()

root.geometry('250x300')

for i in range(0, 4):
    root.columnconfigure(i, minsize=50)

for i in range(0, 7):
    root.rowconfigure(i, minsize=40)

root.configure(background="Black")

root.title("Calculator")

'#Defining Elements'

num = ''
number1 = ''
number2 = ''
text = StringVar()
current = ''

'#Funtions of buttons'

'#Zero Button'


def zero():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '0'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '0'
        text.set(number1)
        print(number1, number2)


'#One Button'


def one():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '1'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '1'
        text.set(number1)
    print(number1, number2)


'#Two Button'


def two():
    global text
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '2'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '2'
        text.set(number1)
    print(number1, number2)


'#Three Button'


def three():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '3'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '3'
        text.set(number1)
    print(number1, number2)


'#Four Button'


def four():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '4'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '4'
        text.set(number1)
    print(number1, number2)


'#Five Button'


def five():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '5'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '5'
        text.set(number1)
    print(number1, number2)


'#Six Button'


def six():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '6'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '6'
        text.set(number1)
    print(number1, number2)


'#Seven Button'


def seven():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '7'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '7'
        text.set(number1)
    print(number1, number2)


'#Eight Number'


def eight():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '8'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '8'
        text.set(number1)
    print(number1, number2)


'#Nine Number'


def nine():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '9'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '9'
        text.set(number1)
    print(number1, number2)


'#Point Symbol'


def point():
    global number2
    if Addition or Subtraction or Division or Multiplication:
        number2 = number2 + '.'
        text.set(number2)
    else:
        global number1
        number1 = number1 + '.'
        text.set(number1)
    print(number1, number2)


'#Symbols'


Addition = False
Subtraction = False
Multiplication = False
Division = False

'#Funtions of Symbols'


def reset():
    global number1, number2, num, text
    num = ''
    number1 = ''
    number2 = ''


def equal():
    global number1
    global number2
    global num
    global Addition
    global Subtraction
    global Multiplication
    global Division
    if Addition:
        num = float(number1) + float(number2)
        Addition = False
    if Subtraction:
        num = float(number1) - float(number2)
        Subtraction = False
    if Multiplication:
        num = float(number1) * float(number2)
        Multiplication = False
    if Division:
        num = float(number1) / float(number2)
        Division = False
    text.set(num)
    print(num)
    number1 = num
    number2 = ''


def plus():
    global Addition
    Addition = True


def minus():
    global Subtraction
    Subtraction = True


def multiply():
    global Multiplication
    Multiplication = True


def divide():
    global Division
    Division = True


'#Buttons'
ac_button = Button(text="AC", bg="Black", fg="#FF0040", command=reset)
ac_button.grid(column=0, row=1, columnspan=3, sticky="nsew")
times_button = Button(text="/", bg="Black", fg="#FF0040", command=divide).grid(column=3, row=1, sticky="nsew")
divide_button = Button(text="X", bg="Black", fg="#FF0040", command=multiply).grid(column=3, row=2, sticky="nsew")
minus_button = Button(text="-", bg="Black", fg="#FF0040", command=minus).grid(column=3, row=3, sticky="nsew")
plus_button = Button(text="+", bg="Black", fg="#FF0040", command=plus).grid(column=3, row=4, sticky="nsew")
equal_button = Button(text="=", bg="Black", fg="#FF0040", command=equal).grid(column=3, row=5, sticky="nsew")
point_button = Button(text=".", bg="Black", fg="#FF0040", command=point).grid(column=2, row=5, sticky="nsew")
zero_button = Button(text="Zero", bg="Black", fg="#FF0040", command=zero)
zero_button.grid(column=0, row=5, columnspan=2, sticky="nsew")
one_button = Button(text="1", bg="Black", fg="#FF0040", command=one).grid(column=0, row=4, sticky="nsew")
two_button = Button(text="2", bg="Black", fg="#FF0040", command=two).grid(column=1, row=4, sticky="nsew")
three_button = Button(text="3", bg="Black", fg="#FF0040", command=three).grid(column=2, row=4, sticky="nsew")
four_button = Button(text="4", bg="Black", fg="#FF0040", command=four).grid(column=0, row=3, sticky="nsew")
five_button = Button(text="5", bg="Black", fg="#FF0040", command=five).grid(column=1, row=3, sticky="nsew")
six_button = Button(text="6", bg="Black", fg="#FF0040", command=six).grid(column=2, row=3, sticky="nsew")
seven_button = Button(text="7", bg="Black", fg="#FF0040", command=seven).grid(column=0, row=2, sticky="nsew")
eight_button = Button(text="8", bg="Black", fg="#FF0040", command=eight).grid(column=1, row=2, sticky="nsew")
nine_button = Button(text="9", bg="Black", fg="#FF0040", command=nine).grid(column=2, row=2, sticky="nsew")
text_display = Entry(textvariable=text, bg="Black", fg="#FF0040").grid(row=6, columnspan=4)

'#End'
root.mainloop()
