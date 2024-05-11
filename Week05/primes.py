#Week05
#Programme to generate prime numbers - test numbrs between 2 and 100 if divisible by int and returns int
#Author Darragh Brennan

primes = []
upto = 10000
for candidate in range (2, upto):
    #   print (candidate)

    isPrime =True #determine if prime, boolean true false loop do divide each value in list
    for divisor in primes: 
         #(2, candidate): # if number in list if divisible by numbers starting at 2 up to the candidate number,  if yes not prime,  if no numbert is prime - only divislbe by 1 or itself
        if (candidate % divisor == 0):
            isPrime = False
            break
    if isPrime:
            primes.append(candidate)
print (primes)