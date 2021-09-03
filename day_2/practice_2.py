# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5

# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!

user_input = input("Pick a number from 1 - 9: ")
int_user_input = int(user_input)

mult = int_user_input * 2
print(mult)

add = 10 + mult
print(add)

div = add / 2
print(div)

sub = div - int_user_input
print(sub)

