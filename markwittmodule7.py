#Mark Witt, Module 7 Assignment
#create a program using a while loop to determine how long it takes for an investment to double at a given interest rate
#user input will be the initial investment and annualized interest rate. Output will be number of years to double initial investment

#loop counter: this will be how many years (how many times) the math loop is ran to get our doubled amount. 
loopCounter = 0

#get user inputs and set up variables
iniitalInvestment = float(input("\nEnter Initial Investment:  "))
interestAPYpercent = float(input("Enter Annualized Interest Rate in percent: "))
interestRate = interestAPYpercent / 100     #take percentage and convert into decimal 
totalAmount = iniitalInvestment
doubleAmount = iniitalInvestment * 2


 #while total amount is less than double initial investment, do the math for one year, add a year to the counter, and compare again.
while totalAmount < doubleAmount:                          
    totalAmount = totalAmount * interestRate + totalAmount
    loopCounter = loopCounter + 1
else: #when total amount is finally double the initial amount: stops the loop and prints the formatted output:
    outputString = f"\nIt will take {loopCounter} years to double your initial investment of ${iniitalInvestment:,.2f} with an APY of {interestAPYpercent:.2f}%,\nand your final total will be ${totalAmount:,.2f}\n"
    print(outputString)

