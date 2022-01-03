import sys
import datetime
import random
import math
import os

def divisor(n :int) -> list:
    i = 1
    lst = list()
    while i <= math.sqrt(n):
        if (n % i == 0):
            if (n / i == i):
                lst.append(i)
            else:
                lst.extend((i, int(n / i)))
        i = i + 1
    lst.sort()
    return lst

def brain(user): #user: input của người dùng
    user = user.lower()
    if user == "help":
        st = '''
Try Command:\nwhich language do you speak?
hello
what is your/my name?
what is the date today?
what time is it now?
president
divisor
convert $ to vnd
swap number
start notepad, cmd, word
random number, letter
'''
        print(st.strip())
    if user == 'which language do you speak?':
        print("I speak English")
    if user == 'hello' or user == 'hello world' or user == 'hi':
        print("hello there")
    if user == 'what is the date today?':
        print("Today's date:", datetime.date.today())
    if user == 'what time is it now?':
        print("Look at the clock in the bottom")
    if user == 'president':
        print("Joe Biden")
    if user == 'you idiot!':
        print("I'm sorry")
    if user == 'divisor':
        try:
            n = int(input("Your number: "))
            lst = divisor(n)
            for i in lst:
                print(i, end = ' ')
        except:
            print("Fake number")
    if user == 'convert $ to vnd':
        try:
            dola = int(input("$ = "))
            gtridola = 23000
            print("VND = ", dola*gtridola)
        except:
            print("Fake number")
    if user == 'swap number':
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            a, b = b, a
            print("Swap Complete")
            print("a = ", a)
            print("b = ", b)
        except:
            print("Fake number")
    if user == 'start notepad':
        os.system("start notepad")
    if user == 'start cmd':
        os.system("start cmd")
    if user == 'start word':
        os.system("start winword")
    if user == 'random number':
        try:
            a = int(input("First Number: "))
            b = int(input("Last Number: "))
            print("Number: ", random.randint(a,b))
        except:
            print("Fake number")
    if user == 'random letter':
        letter = chr(random.randint(65, 123))
        print("Dảk Letter: ", letter)
    if user == 'exit' or user=='bye':
        sys.exit()
    if user == 'what is your name?':
        print("My name is Huân Rose")
    if user == 'what is my name?':
        print(input("Enter your name: "))
    print()