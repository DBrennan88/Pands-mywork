#Week03
#Programme to read in string and strip out leading or trailing spaces 
#Author Darragh Brennan

nameString = "Darragh and Oscar went TO the bEAch in Gresystones"
normalisedString = nameString.strip().lower()

lengthOfnameString = len(nameString)
lengthOfnormalisedString = len(normalisedString)

print (f"That string normalised is : {normalisedString}")
print (f"We rediced the input from {lengthOfnameString} to {lengthOfnormalisedString} charachters")
                       
