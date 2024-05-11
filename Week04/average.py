#Week04
#Programme to read numbers until user enters 0 - append onto a list - print out each number entered and average them
#Author Darragh Brennan

numbers = []

##first number then we check if its 0 in the while loop

number = int() ## zero  quits programme

while number != 0:
    numbers.append(number)

    ## rean next number check if 0

number = int(input("Enter another number, or 0 to quit"))

for value in numbers :
    print (value)

average = float(sum(numbers)) / len.numbers

print (f" the average is {average}")
