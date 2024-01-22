#Mark Witt
#CSD205 Module 4 Assignment - truples

#initialize truple with values:
states = ("alabama", "alaska", "arizona", "arkansas", "california", "colorado", "delaware", "florida", "georgia", "hawaii", "idaho", "indiana", "kentucy", "maine", "michigan", "missouri", "nebraska", "nevada", "new mexico", "north carolina", "ohio", "oklahoma", "south carolina", "tennessee")

#print assignment info:
print('\n' 'Mark Witt' '\n' 'CSD205 Module 4 Assignment: Truples' '\n')

#print truple with new line after:
print('Truple of States: ' '\n')
print(states, '\n')

#print truple without comma formatting, with new line and after:
print('Truple of states, formatted:' '\n')
print(*states, '\n')

#print iteration of each state in a complete sentance:
print('Iterated Truple of States, formatted in a complete sentance:' '\n')
for state in states:
    print(f'I have been to {state.title()}')
print('\n') # print new line for spacing

#print truple in reverse order
print('Iterated Truple of States, in reverse order:' '\n')
print(*states[::-1], sep = '\n')
print('\n') #print new line for spacing

#print iteration of each state in a complete sentance, in reverse order:
print('Iterated Truple of States, formatted in a complete sentance and in reverse order:' '\n')
for state in states[::-1]:
        print(f'I like {state.title()}')
print('\n') #new line for spacing

# AND now just for a little fun: print trouple in sentance, reverse order, 
# and everything is COMPLETELY backwards:
print('And just for a little fun:' '\n' 'Iterated Truple of States, formated in sentances, in reverse order, and EVERTHING is backwards:' '\n')
for state in states[::-1]:
    print(f'I like {state.title()}'[::-1])