import sys
import time


while True:
    while True:
        try:
            time.sleep(1)
            tmath = float(input('hello! what type of math do you want to do?\n 1. add\n 2. subtract\n 3. multiply\n 4. divide\n 5. quit\n '))
            break
        except ValueError:
            print('type a number.')
            time.sleep(2)
    
    if tmath == 1:
        print('You chose addtion!')
        
        while True:
            try:
                num1 = float(input('what is the first number you want to add?\n'))
                break
            except ValueError:
                print('type a number.')
                time.sleep(2)
        while True:
            try:
                num2 = float(input('what is the second number you want to add?\n'))
                break
            except ValueError:
                print('type a number.')
                time.sleep(2)
                
        print(f'{num1} + {num2} = {num1+num2}')

    if tmath == 2:
        print('You chose subtraction!')
        while True:
            try:
                num1 = float(input('what is the first number you want to subtract?\n'))
                break
            except ValueError:
                print('type a number.')
                time.sleep(2)
        while True:
            try:
                num2 = float(input('what is the second number you want to subtract?\n'))
                break
            except ValueError:
                print('type a number.')
                time.sleep(2)
                
        print(f'{num1} - {num2} = {num1-num2}')

    if tmath == 3:
        print('You chose multiplaction!')
        while True:
            try:
                num1 = float(input('what is the first number you want to multiply?\n'))
                break
            except ValueError:
                print('type a number.')
                time.sleep(2)
        while True:
            try:
                num2 = float(input('what is the second number you want to multiply?\n'))
                break
            except ValueError:
                print('type a number.')
                time.sleep(2)
                
        print(f'{num1} * {num2} = {num1*num2}')

    if tmath == 4:
        print('You chose divison!')
        while True:
            try:
                num1 = float(input('what is the first number you want to divide?\n'))
                break
            except ValueError:
                print('type a number.')
                time.sleep(2)
        while True:
            try:
                num2 = float(input('what is the second number you want to divide?\n'))
                break
            except ZeroDivisionError:
                print('you cant divide with zero!')
                time.sleep(2)
            except ValueError:
                print('type a number.')
                time.sleep(2)
                
        print(f'{num1} / {num2} = {num1/num2}')

    elif tmath == 5:
        while True:
            close1 = input('are you sure you want to close out?\n (y/n)\n')
            if close1 == 'y':
                print('ok!')
                sys.exit()
            elif close1 == 'n':
                print('more math!')
                break
            else:
                print('type y or n')

    