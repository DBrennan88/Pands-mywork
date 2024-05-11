#Week05
#Programme to pull 10 random numbers in a list and output all values in list
#take a number, print it and show remainging numbers still in que  - countdownesque?
#Author Darragh Brennan

import random

queue = []
rangefrom = 0
rangeto = 100
numbersinqueue = 10

for n in range(0, numbersinqueue):
    queue.append(random.randint(0, rangeto))

print (f"queue is {numbersinqueue}")
