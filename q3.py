from ast import arg

def string_to_string(argument): #alternative to switch case in Java
    switcher = {
        "CSC1009": "Object-Oriented Progamming" #maps "CSC1009" to "Object-Oriented Programming"
    }
    return switcher.get(argument,"Nothing") #default return if module code cannot be found

module_code="CSC1009" #instantiate module code to be "CSC1009"
print(string_to_string(module_code)) #print output based on module code
    

for x in range(101,66,-2): #print all values between 101 and 66, decrementing by 2 each time
    print("Value of x is:",x) #print value of x