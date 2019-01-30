#help https://pynative.com/python-check-user-input-is-number-or-string/

from termcolor import colored, cprint
import time 
#dghbdbhdxgbv
cprint("hello",'red',attrs=['blink'])
#cprint()
myvar = 0
goalvar = 50
bigvar = "myvar is bigger"
smallvar = "myvar is smaller"

def checkit(): 
    try:
        #val =float(myvar)
        myvar = float(input('imput a number:'))
        if myvar>goalvar:
            print(bigvar)
        else: 
            print(smallvar)
    except ValueError:
        print("That's not a number!")
        time.sleep(2)
        print("lets try that again..")
        time.sleep(2)
        #myvar = float(input('Try again:'))
        checkit() 

checkit()
