def getDetails(name = "Sean",state = "Guest"):
    print(f"Name is {name} and State is {state}")

# no parameter
getDetails()

 # single argument assumed to be for the first parameter
getDetails("Sean")   

# single keyword argument
getDetails(state = "member")

#2 keyword arguments
getDetails(name = "John", state = "Member")
