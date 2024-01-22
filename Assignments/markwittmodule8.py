#Mark Witt, Module 8
#A program to convert user inputed miles driven into kilometers via a function and to validate user input using try/except methods

#import time for output timing and delay 
import time

#main menu options dictionary:
menuOptions = {
    1 : 'Convert Miles to Km',
    2 : 'Exit'
}

#main menu function:
def print_menu():
    print('\nWhat would you like to do?')
    for key in menuOptions.keys():  
        print(key, '--', menuOptions[key])

#convert and format output string function, returns final output string:
def convert(totalMiles):
    totalKm = totalMiles * 1.609344
    returnString = f'{totalMiles:,.2f} Mi is equivilant to {totalKm:,.2f} Km.'
    return returnString

#get user input, validate, call convert function and print the returned output string:
def MileToKM():
    #try/except input and validation:
    while(True):    
        try:
            totalMiles = float(input('\nPlease enter total miles driven: '))
        except ValueError:
            print("Invalid Input. Please enter a numerical value.")
            continue
        else:
            break
    print('\nCalculating...\n')
    time.sleep(1.5)
    #call convert funciton and print returned output string:
    print(convert(totalMiles))
    time.sleep(1.5)

#main menu:
while(True):
    print_menu()
    while(True):
        try:
            option = int(input("Enter Selection>> "))
        except ValueError:
            print("\nInvalid Input. Please enter a numerical value.")
            print_menu()
            continue
        else:
            break
    if option == 1:     #Option for calling miles to km calculator
        MileToKM()
    elif option == 2:   #Exit menu/program option
        print("\nThanks for using Eagle Eye calculator!\nGoodbye.\n")
        exit()
    else:
        print('\nInvalid Option. Please choose again.\n') #error selecting menu options, please try again!
