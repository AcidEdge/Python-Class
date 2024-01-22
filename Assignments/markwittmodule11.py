#Mark Witt - 09/21/2022
#Module 11 Assignment utilizes module 9
#banking program using parent and child classes 
#account balances, fees, minimum balance and interest rate is set at begining of program to make iteration through the program easier.
#checking account is initially set to $25, so minimum balance will be checked. once checking balance goes above min balance, balance warning will not be displayed
#savings account initially set to 200, and when checking balance will display amount of interst that will be added on the first of each month
#if the current date is the first of the month then fees are deducted from checking account, and interest is added to savings account. 
#for date fuctionality testing, replace the .now on line 192 with (2022, 10, 1) ***year, month, day*** so the program will think it is the frist of the month and will apply fees/interest. Any first of the month can be used
#hint - bug does not have anything to do with the dates or line 192. bug is rather simple, but prevents program from running. 

import datetime
import time
from os import system, name

checkingBalance = 25
savingsBalance = 200
checkingFees = 5
minBalance = 50
intereset = 0.02
checkAccountNumber = 1234356
savingAccountNumber = 9987653

#define clear screen method:    This will clear the terminal screen using either cls for windows, or clear for mac / linux
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#define pause method:
#pauses program, and clears the screen after user pushes enter button
def pause():
    programPause = input('\n\nPlease press ENTER to continue')
    clear() 
    

#set up main menus:
#these are broken up for ease of display and readability
mainMenu = {    #this one is for checking
    1 : 'Withdrawl',
    2 : 'Deposit',
    3 : 'Check Balance'
}

selectMenu = {  #this one is for savings
    4 : 'Withdrawl',
    5 : 'Deposit',
    6 : 'Check Balance'
}

otherMenu = {       #exit program option
    7 : 'Exit'
}

#main menu function:
def print_main_menu():
    clear()
    today = datetime.datetime.now() #get today date and time
    print(f'Welcome.\nToday is', today.strftime("%B %d, %Y"),'\n\nWhat would you like to do?')
    print('\nChecking Account Options:\n')
    for key in mainMenu.keys():  
        print(key, '--', mainMenu[key])
    print('\nSavings Account Options:\n')
    for key in selectMenu.keys():
        print(key, '--', selectMenu[key])
    print('\nOther Options:\n')
    for key in otherMenu.keys():
        print(key, '--', otherMenu[key])




#create BankAccount Class:
class BankAccount:
    def __init__(self, accountNumber, balance, accountType, today):
        self.accountNumber = accountNumber #what is a bank account without having account numbers, passed in to use with output
        self.balance = balance  #account balance, passed in as checkingBalance or savingsBalance, depending on object created
        self.accountType = accountType #used to pass type of account, checking or savings, into outputs. 
        self.today = today  #used to get todays date, to output when interest/fees will be applied, and to test if it is the 1st of the month to apply the fees/interest


    #withdrawl method:    
    def withdrawl(self):
        while(True):
            try:   #enter withdrawl amount, error check if it is numerical, and verify there are sufficent funds to withdraw
                withdraw = int(input("Enter Withdrawl Amount -- $"))
            except ValueError:
                print("\nInvalid Input. Please try again with a numerical value.")
                continue
            if withdraw > self.balance:
                print(f"\nInsufficient Funds. Your {self.accountType} account balance is:\n ${self.balance:,.2f}.")
                continue
            else:
                break
        self.balance = self.balance - withdraw  #withdraw requested amount from account, then display withdrawl recap, including account number and balance
        print(f"\n${withdraw:,.2f} has been withdrawn from {self.accountType} account number {self.accountNumber}.")
        print(f"Your new balance is:\n${self.balance:,.2f}\n")

    
    
    #deposit method:
    def deposit(self):
        while(True):
            try:    #get deposit amount input, validate input is numerical value and is not negative
                deposit = int(input("Enter Deposit Amount -- $"))
            except ValueError:
                print("\nInvalid Input. Please try again with a numerical value.")
                continue
            if deposit < 0:
                print("\nError: Cannot Depost a negative amount! Please try again with a positive amount.")
                continue
            else:
                break
        self.balance = self.balance + deposit   #deposit inputed amount into account, then display deposit recap with account numner and balance
        print(f"\nThank you for your deposit of ${deposit:,.2f} \ninto {self.accountType} account number {self.accountNumber}")
        print(f"Your new balance is: ${self.balance:,.2f}\n")
 
    
    #get balance method:    displays current balance and account number
    def getBalance(self):
        print(f'\nYour current balance for {self.accountType} account number {self.accountNumber} is:\n ${self.balance:,.2f}\n')

        
#create child class for checking account:
class CheckingAccount(BankAccount):
    def __init__(self, accountNumber, balance, accountType, today, fees, minimumBalance, applied):
        super().__init__(accountNumber, balance, accountType, today)      #inherits variables and methods from parent BankAccount Class
        self.fees = fees        #value passed into object for bank account fees, charged to account on the 1st of the month if account balance is less than the minimum balance
        self.minimumBalance = minimumBalance   #minimum balance amount determined by bank. used to determine if fees need to be charged to the checking account 
        self.applied = applied  #used to determine if fees have been applied for the month or not. boolean, False if fees not applied yet, set as True once applied

    #deduct fees 
    def deductFees(self):   #will only be called from checkMinBalance when it is the first of the month, 
        addAdditionalDeposit = self.minimumBalance - self.balance   #calculates additional deposit required to avoid next months fees
        if self.applied == False:   #check if fees have already been applied. False if they have not, True if they have.
            self.balance = self.balance - self.fees     #deducts fees
            self.applied = True         #set as True so fees are not deducted again for the month
            
            print('Today is', self.today.strftime("%B %d, %Y"))
            print(f'{self.fees:,.2f} in fees have been deducted from your {self.accountType} account because your balance of ${self.balance:,.2f} is less than the required minimum balance of ${self.minimumBalance:,.2f}.')
            print(f'Please deposit an additional ${addAdditionalDeposit:,.2f} to avoid future fees related to minimum balance.')
        else:
            print(f'A fee of ${self.fees:,.2f} has already been applied to {self.accountType} account number {self.accountNumber} for the month of', self.today.strftime('%B'),'.')
            print(f'Please deposit an additional ${addAdditionalDeposit:,.2f} before', (today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1).strftime("%B %d, %Y"), 'to avoid next fees for next month.')
        

    #check minimum balance:
    #checks minimum balance vs actual balance. calls the deductFees method if balance is less than minimum, it is the 1st of the month. 
    #if critieria for calling deductFees is not met, it will warn account holder that X amount must be deposited before the 1st of month to avoid fees for minimum balance.
    def checkMinBalance(self):      
        
        addAdditionalDeposit = self.minimumBalance - self.balance
        if self.balance < self.minimumBalance:      #evaluate minimum balance fee criteria, if conditions are met, calls deductFees method
            if self.today.day == 1:
               
                self.deductFees()
                
            else:   #warning to user that they must deposit additional amount to prevent being charged minimum balance fees, and what date they will be charged:
                print(f'\n\n***WARNING***\nFor {self.accountType} account number {self.accountNumber}:\nYour balance of ${self.balance:,.2f}\nis less than the minimum required balance of ${self.minimumBalance:,.2f}')
                print(f'Please deposit an additional ${addAdditionalDeposit:,.2f} before:')
                print((today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1).strftime("%B, %d, %Y"))   #prints date for first of next month. math/formulation originated from PyQuestions.com, https://pyquestions.com/how-can-i-get-the-first-day-of-the-next-month-in-python
                print(f'to avoid {self.accountType} fees of ${self.fees:,.2f}. ')
        else:
            pass
            

#create child class for savings account:
class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, balance, accountType, today, interestRate, applied):
        super().__init__(accountNumber, balance, accountType, today)
        self.interestRate = interestRate    #monthly interest rate value
        self.applied = applied  #used to check if interest has already been applied for the month. Boolean, False if interest has not been added for the month yet, True if it has
    
    def addInterest(self):
        #method for determining amount of earned interest, and when to apply it (must be 1st of the month and have not been deposited yet.)
        addedInterest = self.balance * self.interestRate    #calculates how much interest will be added on the 1st of the month
        if self.today.day == 1:
            if self.applied == False:   #check if interest has already been applied for the current month. False if not, True if they already have
                self.balance = self.balance + addedInterest
                print(f'Your {self.accountType} account number {self.accountNumber} has earned ${addedInterest:,.2f}.\nYour new balance is: ${self.balance:,.2f}')
                print(f'Your current interst rate is:', self.interestRate * 100, '%')
                self.applied = True #applies interest to savings account and then sets as true so it will not continue to apply interest multiple times for the month.
            else:   #if interest already applied, gives this message:
                print(f'Interest for the month of', today.strftime('%B'))
                print(f'has been applied to your {self.accountType} account in the amount of: ${addedInterest:,.2f}')
                print(f'Your current interst rate is:', self.interestRate * 100, '%')
        else:   #message to user detailing next amount of interest and when it will be applied to savings account:
            print(f'Your {self.accountType} account number {self.accountNumber} will earn ${addedInterest:,.2f} in interest on:')
            print((today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1).strftime("%B, %d, %Y"))
            print(f'Your current interst rate is:', self.interestRate * 100, '%')

#create instance of objects/classes:
today = datetime.datetime.now()
checkObject = CheckingAccount(checkAccountNumber, checkingBalance, 'Checking', today, checkingFees, minBalance, False)
saveObject = SavingsAccount(savingAccountNumber, savingsBalance, 'Savings', today, intereset, False)

#run menu and program:
while(False):
    print_main_menu()
    while(True):    #menu loop
        try:
            option = int(input("\nEnter Selection>> "))
        except ValueError:
            print("\nInvalid Input. Please enter a numerical value.")
            time.sleep(1.5)
            clear()
            print_main_menu()
            continue
        else:
            break
    if option == 1:     #Option for choosing checking account withdrawl
        clear()
        checkObject.withdrawl()
        checkObject.checkMinBalance()
        pause()

    elif option == 2:   #option for choosing checking account deposit
        clear()
        checkObject.deposit()
        checkObject.checkMinBalance()
        pause()

    elif option == 3:   #option for getting checking account balance, also will check/add interest
        clear()
        checkObject.getBalance()
        checkObject.checkMinBalance() 
        pause()

    if option == 4: #option for savings account withdrawl
        clear()
        saveObject.withdrawl()
        pause()

    if option == 5:     #option for savings account deposit
        clear()
        saveObject.deposit()
        pause()

    if option == 6:     #option for getting savings account balance, as well as will check/add interest
        clear()
        saveObject.getBalance()
        saveObject.addInterest()
        pause()

    if option == 7:   #Exit menu/program option, with a little matix easter egg fun added.
        clear()
        print("\nThanks for using Eagle Eye Banking!")
        time.sleep(1.75)
        clear()
        print('\nFollow the White Rabbit.')
        time.sleep(1.75)
        clear()
        print('\nKnock Knock, Neo.')
        time.sleep(1.5)
        clear()
        exit()
    if option > 7:
        print('\nInvalid Option. Please choose again.\n') #error selecting menu options, please try again!
        time.sleep(1.75)
        clear()

