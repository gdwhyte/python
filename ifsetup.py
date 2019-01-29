#help https://pynative.com/python-check-user-input-is-number-or-string/

from termcolor import colored, cprint

cprint("hello",'red',attrs=['blink'])
#cprint()
myvar = float(input(':'))
#myvar = input('imput a number:')

try:
    val =float(myvar)
except ValueError:
    print("not a number!")
    myvar = float(input('Try again:'))
bigvar = "myvar is bigger"
smallvar = "myvar is smaller"

def funcname(self, parameter_list):
    pass

def checkit():
    if type(myvar) == str: print("no!")
    else: 
        if myvar>1:print(bigvar)
        else: print(smallvar) 

checkit()
#if type(myvar) == str: print("no!")

