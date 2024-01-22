from calendar import calendar
import datetime
import calendar
from os import system, name


def pause():
    programPause = input("Press ENTER to continue.")
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

    
#testing validate string length:
while(True):
        try:
            userPhone = int(input('Please enter phone number(10 digits, no dashes/spaces): '))
            phoneNum = '{}'.format(userPhone)
        except ValueError:
            print('\nError:\nEntry was NOT a phone Number. Please try again')
            continue
        if len(phoneNum) != 10:
            print('\nError:\nEntry was not 10 digits. Please try again. ')
            continue
        else:
            break
a = phoneNum[0]+phoneNum[1]+phoneNum[2]
b = phoneNum[3]+phoneNum[4]+phoneNum[5]
c = phoneNum[6]+phoneNum[7]+phoneNum[8]+phoneNum[9]
userNumber = '('+a+') '+b+'-'+c
print(userNumber)