#created by kibrom kifle
#edited by hala
from random import randint

rand = randint(1,10)
guess = True

while guess:
    num = int(input("Enter enteger number 1-10: "))
    if num>rand:
        print('guess lower')
    elif num<rand:
        print('guess higher')
    if num==rand:
        print('you got the number')
        guess=False
