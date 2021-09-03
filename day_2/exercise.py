# ITP Week 1 Day 2 Exercise

# Take an user's input for his age

# The user input comes in as a string so we have to cast it to a int!

# Use an if/else to determine if they are of legal drinking age.
# if the user is of age, print "Welcome!"
# else, tell them to come back in X amount of years (use math operations)

# Bonus: Add a validation by checking the type of the user input
# to ensure it can be casted as an int. Handle any other input that
# are not numbers to try again.


user_age = input("Please enter your age: ")

if(int(user_age) <= 20):
    X =  21 - int(user_age) 
    print("Come back in " + str(X) + " years.")
else:
    print("Welcome!")






if(type(user_age) is str): #Validation for casting (BONUS)
     print("It can be casted as an int.")

else:
     print("It cannot be casted as an int.")


