#Week05
#Programme  -  whats wrong here ? 
#Author Darragh Brennan

numberofQuestions = 5
averageAge = 23.4
debugMode = True
name = "Darragh"
ages = []
months = ("Jan", "Feb", "March")
books = {}
stuff = [12, "Fred",  False, {}]
someone = dict(firstname = "Darragh")
'''me = {
    "firstname" : "Darragh", 
    "studying" :  [
        {  "courseName" : "programming", 
        "semester" : 1} , 
        {"courseName": "Data Represenatation", 
    "semester" : 2
    }
 ]
}
'''
me = {
    "firstname" : "Darragh",
    "studying" : [
        {"semester" : "1", "courseName" : "programming"}, 
        {"semester" : "2", "courseName" : "Data Analytics" }
    ] 
 }


## find th types of variables

print (type(numberofQuestions))
print (type(averageAge))
print (type(debugMode))
print (type(name))
print (type(ages))
print (type(months))
print (type(books))
print (type(stuff))
print (type(someone))
print (me["firstname"])
print (me["studying"])