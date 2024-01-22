#Mark Witt, 8/29/2022, Module 5 Assignment
#modify module 3 assignment to use if/else inorder to charge
#different amounts, giving discounts for longer length of cable


from operator import truediv
from pickle import TRUE
import time #used for pausing program so user can read output before returning to main menu

#dictionary of menu options:
meunOptions = {
    1: 'Enter length of cabling',
    2: 'Exit',
}


#object for entering cable and company information:
def enterCable():
    print("Please enter the following information:\n")
    companyName = input("Company Name: ")                            #input for company name
    requestedLength = float(input("Cable length needed: "))         #input for length of cable requested
        
    priceOptions = {0:0.87, 1:0.8, 2:0.7, 3:0.5}            #dictionary of pricing
    lengthOptions = {0:100, 1:250, 2:500}                   #dictionary of cable length
    cableRate = 0


    #evaluate lentgh options and calculate cost:
    if requestedLength  < lengthOptions[0]:                                                #evaluate if requested length is less than 100 ft
        totalCost = requestedLength * priceOptions[0]                                       #calculate total cost
        cableRate = priceOptions[0]
    elif requestedLength >= lengthOptions[0] and requestedLength < lengthOptions[1]:        #evaluate if requested length is between 100 and 250 ft
        totalCost = requestedLength * priceOptions[1]                                       #calculate total cost
        cableRate = priceOptions[1]
    elif requestedLength >= lengthOptions[1] and requestedLength < lengthOptions[2]:        #evaluate if requested length is between 250 and 500 ft
        totalCost = requestedLength * priceOptions[2]                                       #calculate total cost
        cableRate = priceOptions[2]
    else:                                                                               #anything 500 ft and over
        totalCost = requestedLength * priceOptions[3]                                   #calculate total cost
        cableRate = priceOptions[3]
    
    #display calucated cost:
    OutputString = f"\n{requestedLength:.2f} feet of cable will cost {companyName.title()}:\n\t\t${totalCost:.2f}\nWith a rate of ${cableRate:.2f} per foot. "
    print(OutputString)
    
    
    #pause program then returns to main menu to allow multiple repitition:
    time.sleep(2.5)

#method for overall main menu:
def print_menu():
    print('\nWhat would you like to do?')
    for key in meunOptions.keys():  
        print(key, '--', meunOptions[key])


#main menu code: program starts here, when option 1 selected goes to cable length object, when option 2 is selected - thanks and exits program, includes error check with return to menu         
while(True):
    print_menu()
    option = int(input('Enter choice: '))

    if option == 1:     #Option for entering cable length order
        enterCable()
    elif option == 2:   #Exit menu/program option
        print("Thanks for using Eagle Eye Cabling's order center!\nGoodbye.")
        exit()
    else:
        print('\nInvalid Option.\n') #error selecting menu options, please try again!
