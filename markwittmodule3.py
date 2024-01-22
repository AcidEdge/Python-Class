# Mark Witt, 8/17/2022, Module 3 Assignemnt
# Program to calculate the cost of installing fiber optic cable
# at a cost of $0.87 for stated company

#display program text:
print("Welcome to Eagle Eye Cabling's Cost Calculator!")
print("Please enter the following information-")

#get company name:
CompanyName = input("Company Name: ")

#get cable length and specify as a floating number
CableLength = float(input("Length of fiber optic cable needed: "))

#calculate cost:
CableCost = CableLength * 0.87

#print blank line
print()

#create and format output as a string then displays the string
#output of info:      :.2f rounds to 2 decimal places   #.title capitalizes name  #:.2f rounds cost (2 dec places again
OutputString = f"{CableLength:.2f} feet of cable will cost {CompanyName.title()}:\n\t\t${CableCost:.2f}"
print(OutputString)

#output a thank you to the user
print()
print()
print("Thank you for choosing Eagle Eye Cabling!")

