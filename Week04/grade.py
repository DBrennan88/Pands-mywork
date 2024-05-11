#Week04
#Programme that reads students % mark print correspondinf grade - program check % is valid
#Author Darragh Brennan

percentage  = float(89)

## define % banding with corresponding grade
if percentage < 0 or percentage > 100:
    print ("Please enter number between 0 and 100")  ##exception handling function 

elif percentage < 40:
    print ("Fail")

elif percentage < 50:
    print ("Merit")

elif percentage < 60:
    print ("Merit1")

elif percentage < 70:
    print ("Merit2")

elif percentage > 70:
    print ("Distinction")


