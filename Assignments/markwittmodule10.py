#Mark Witt
#Module 10 Assignment
#program to read and write user input to a file. user inputs file path and file name, and allows user to write to the file(append), read the file, or delete the file.
#program error checks inputs, including if file exists errors when trying to read or delete, and validates inputs (numerical values, and length of phone number (10 digits))

from os import system, name
import os
import datetime
import time

#main menu dictionary:
mainMenu = {
    1 : 'Write to a file',
    2 : 'Read a file',
    3 : 'Delete a file',
    4 : 'Exit'
}

#print menu function:
def printMenu():
    clear()
    today = datetime.datetime.now()
    print(f'Today is {today.strftime("%B %d, %Y")}\nWhat would you like to do?')
    for key in mainMenu.keys():
        print(key, '--', mainMenu[key])

#clear screen function:
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
#pause function:
def pause():
    programPause = input('\n\nPlease press ENTER to continue')
    clear() 

#get file name and path funciton:
def getFileInfo():
    clear() #get file path and file name:
    filePath = input('Please enter file path: ')
    fileName = input('Please enter file name: ')
    global completePath #use completePath gobal variable
    completePath = filePath+fileName    #sets final path/file

#write data function: gets data input from user, validate input and writes to file. reads file back to user for conformation afterwards
def writeData():    
    clear() #get data to write into file:
    userName = input("Please enter name: ")
    userAddress = input("Please enter address: ")
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
    commaSpace = ', '   #comma seperators
    newLine = '\n'      #new line for string, makse sure new data is written to a new line each time
    userData = userName.title()+commaSpace+userAddress.title()+commaSpace+userNumber+newLine #sets final data string, all fields combined
    clear()
    #open file and write data, then reads the file back to the user
    with open(completePath, 'a') as fileHandle:
        fileHandle.write(userData)
    readFile()

#read file funciton: validates if file exists, if true then prints line by line of file
def readFile():
    clear()
    try:
        with open(completePath, 'r') as fileHandle:
            print(f'{completePath} contains the following data:\n')
            for line in fileHandle:
                print(line)
    except FileNotFoundError:
        print(f"Sorry, the file '{completePath}' doesn't exist. \nPlease check the filename and path, then try again.")
    pause()

#delete file function: validates if file exists, if true then deletes the file
def deleteFile():
    clear()
    try:
        os.remove(completePath)
        print(f"The file '{completePath} has been deleted.")
    except FileNotFoundError:
        print(f"Sorry, the file '{completePath}' doesn't exist. \nPlease check the filename and path, then try again.")
    pause()

#run main menu: (with input validation)
while(True):        #menu loop
    printMenu()
    while(True):    
        try:
            option = int(input("\nEnter Selection>> "))
        except ValueError:
            print("\nInvalid Input. Please enter a numerical value.")
            time.sleep(1.75)
            clear()
            printMenu()
            continue
        else:
            break
    if option == 1:
        getFileInfo()
        writeData()
    if option == 2:
        getFileInfo()
        readFile()
    if option == 3:
        getFileInfo()
        deleteFile()
    if option == 4:
        clear()
        print('Thank you for using Eagle Eye file handling.... \n Goodbye!')
        exit()
    if option > 3:
        print('Invalid Selection. Plese try again.')
        time.sleep(1.75)
        clear()