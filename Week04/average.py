#Week04 
#Programme to read numbers until user enters 0 - append onto a list - print out each number entered and average them
#Author Darragh Brennan

numbers = []

##first number then we check if its 0 in the while loop

number = int(input("Enter number (0 to quit): ")) ## zero  quits programme

while number != 0:
    numbers.append(number)
    number = int(input("enter another (0 to quit)"))

    ## rean next number check if 0


for value in numbers:
    print (value)


average = float(sum(numbers)) / len(numbers) 
print (f" the average is {average}")


