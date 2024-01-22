#Mark Witt, Module 6 Assignment
#8-29-2022
#using dictionaries, include 10 key value pairs
#print entire dictionary, have user select a one and print that value paired to that key

import time # for pause to read output after selecting 

#dictionary of planets
planetsInGalaxy = {
    1:'Naboo',
    2:'Alderaan',
    3:'Hoth',
    4:'Jedha',
    5:'Yavin IV',
    6:'Coruscant',
    7:'Bespin',
    8:'Tatooine',
    9:'Bespin',
    10:'Endor'
}

#select again dicionary for selecting again or exiting
selectAgainMenu = {
    1:'Yes',
    2:'No'
}

#create list of user favorites:
userList = []

#select again menu:
def selectAgain():
    print('\nWould you like to choose another?')
    for key in selectAgainMenu.keys():
        print(key, '--', selectAgainMenu[key])
    menuOption = int(input('Enter your choice: '))
    if menuOption == 2:
        print('\nGoodbye old friend!\nMay the Force be with you!')
        exit()
    elif menuOption == 1:
        print('\nOK! Here we go again!\n')
    else:
        print('\nError, that was not an option! Please try again\n')
        time.sleep(1)
        selectAgain()
    
#method for printing list of planets:
def printListofPlanets():
    print('My favorite planets in Star Wars are:')
    for key in planetsInGalaxy.keys():
        print(key, '--', planetsInGalaxy[key].title())


#print list of planets, get user selection, add selection to user list,  and output their selection with sentance
while(True):
    printListofPlanets()
    option = int(input("\nWhat is your favorite?  "))
    print('')
    if option >= 1 and option <= 10:
        userList.append(planetsInGalaxy[option])
        print('Your favorites are:\n')
        for x in userList:
            print(x)
        print('\nThose are great choices!\n')
        time.sleep(2)
        selectAgain()
    else:
        print('\nERROR: Invalid Selection, Please Try Again.\n\n')
        time.sleep(1)
       

