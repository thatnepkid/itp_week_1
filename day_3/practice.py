us_state = ["Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"
]

# 1. Write the code below that verifies the amount (length) of US States!

print(len(us_state))

# 2. Create a variable called 'my_state_index' and assign it to the index of your state.

my_state_index = us_state[4]

# 3. let's see if you were right.. uncomment below and run. Do you see your state?

print("My state is: " + my_state_index)

# 4.Using your state index, let's emphasize some importance to it by *upper*casing it.

print(my_state_index.upper())

# 5. POOF. You've been promoted to President! Let's add a new state. I like my list to be alphabetical (which it is)
# So let's go ahead and create a state that starts with Z and append it to the end of the list.

us_state.append("Z Nation")

# 6. There is no state that begins with B! Lets create one and insert it appropriately. (There are 3 A states.)

us_state.insert(4, "Bamboo")

# 7. Does anyone live in Iowa? Do you know anyone that lives there? Is it even real?! Remove it.. Do it president.

us_state.pop(15)

print(us_state)