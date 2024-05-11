#Week04 Extras
#Programme 
#Author Darragh Brennan


percentage  = float(69.5)                  ##value assigned to variable
round_percentage = round(percentage)       #set logic to round variable value - assigned rounded value to secondary variable 
## define % banding with corresponding grade
if round_percentage < 0 or round_percentage > 100:
    print ("Please enter number between 0 and 100")  ##exception handling function 

elif round_percentage <= 40:
    print ("Fail")

elif round_percentage <= 50:
    print ("Merit")

elif round_percentage <= 60:
    print ("Merit1")

elif round_percentage < 70:   ####set parameters so >=70 is distinction
    print ("Merit2")

elif round_percentage >= 70:
    print ("Distinction")


