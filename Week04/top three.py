#Week04 
#Programme to generate 3 random numbers 0 to 100 - prnt them out - then print top 3
#Author Darragh Brennan

import random

howMany = 10
topHowMany = 3
rangefrom = 0
rangeto = 100

numbers = []

for i in  range (0, howMany) :
    numbers.append(random.randint(rangefrom, rangeto))
print (f"{howMany} random numbers\t {numbers}")

topthree = numbers.copy()
print (f"The top {topHowMany} are t\ {topthree[0:topHowMany]}")

