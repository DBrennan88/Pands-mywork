##While loops   - https://www.w3schools.com/python/python_while_loops.asp

##i = 1
##while i < 6:
  ##print(i)
  ##i += 1


numberToGuess = float (-1)

guess = float (-1)
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("Too high")
    guess = (input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)