# ITP Week 1 Day 2 Lecture

# DATA TYPES

# In programming, data type is an important concept.

# Python has the following data types built-in by default, in these categories:

# Text Type:        str
# Numeric Types:	int, float, complex*
# Boolean Type:	    bool
# Sequence Types:	list, tuple*, range
# Mapping Type:	    dict
# Set Types:	    set*, frozenset*
# Binary Types:	    bytes*, bytearray*, memoryview*

# VARIABLES (CONT.)

# Variables can store data of different types, and different types can do different things.

# In Python, the data type is set when you assign a value to a variable:

# Example	                                        Data Type
# x = "Hello World"	                                str
# x = 20	                                        int
# x = 20.5	                                        float
# x = True	                                        bool
# x = ["apple", "banana", "cherry"]	                list
# x = range(6)	                                    range
# x = {"name" : "John", "age" : 36}	                dict
# x = 1j	                                        complex*
# x = ("apple", "banana", "cherry")	                tuple*
# x = {"apple", "banana", "cherry"}	                set*
# x = frozenset({"apple", "banana", "cherry"})	    frozenset*
# x = b"Hello"	                                    bytes*
# x = bytearray(5)	                                bytearray*
# x = memoryview(bytes(5))	                        memoryview*

# you can always get the type of the variable with type()
print(type("Hello"))
exampleInt = 34
print(type(exampleInt))

# NUMBERS
# - int: or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# - float: or "floating point number" is a number, positive or negative, containing one or more decimals.
# - complex*: combination of a real and imaginary number, written with a "j" as the imaginary part.

# CASTING

# Casting is specifying a type on to a variable.

# Under a mircoscope
    # Since Python is an object-orientated language, it uses classes to define data types, including its primitive types.
    # Casting in python is therefore done using constructor functions

# 5 available casting function
# each which takes in specific arguments
# We will only cover 3.

# 1. int() - constructs an integer number from:
    # - integer literal
    # - float literal (by removing all decimals),
    # - string literal (providing the string represents a whole number)
# 2. float() - constructs a float number from:
    # - integer literal
    # - float literal
    # - string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including:
    # - strings
    # - integer literals
    # - float literals

# The other two are boolean and complex casting.

# PRACTICE 1

# ARITHMETIC OPERTORS

# Operator	Name	        Example
# +	        Addition	    x + y
# -	        Subtraction	    x - y
# *	        Multiplication	x * y
# /	        Division	    x / y
# %	        Modulus	        x % y
# **	    Exponentiation	x ** y
# //	    Floor division	x // y

# we can assign variables to the evaluation of arithmetic operators

sum = 4 + 4
sub = 1 - 100 # it can evaluate to negatives too!
div = 10/5 # even if it divides evenly, it returns a float.
floor = 10//3 # to only get whole numbers, we use floor division.

# ASSIGNMENT OPERATORS

# we can shorthand the assignment of arithmetic operations by using assignment operators.

# Operator	Example	    Same As
# =	        x = 5	    x = 5
# +=	    x += 3	    x = x + 3
# -=	    x -= 3	    x = x - 3
# *=	    x *= 3	    x = x * 3
# /=	    x /= 3	    x = x / 3
# %=	    x %= 3	    x = x % 3
# **=	    x **= 3	    x = x ** 3
# //=	    x //= 3	    x = x // 3

# The arithmetic assignment operators only work on Python Numbers.

x = 3
x += 6
print(x) # 9

y += 3
# NameError: name 'y' is not defined

y = "3"
y += 3
# TypeError: can only concatenate str (not "int") to str

# BOOLEANS

# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)

# We can also use the bool() function
# which allows you to evaluate any value,
# and give you True or False in return

print(bool("Hello")) # True
print(bool(15)) # True
print(bool("")) # False
print(bool(0.0)) # False

# According to the Python Documentation:
# By default, an object is considered true.

# COMPARISON OPERATORS

# Comparison operators are used to compare two values:

# Operator	Name	Example
# ==	Equal	                    x == y
# !=	Not equal	                x != y
# >	    Greater than	            x > y
# <	    Less than	                x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	    x <= y

a = 4
b = 5
c = 5
a == b # False
b == c # True
a != b # True
b != c #False
a > b # False
b > c # False
a < b # True
b < c # False
a >= b # False
b >= c # True
a <= b # True

# LOGICAL OPERATORS

# Operator	Description	Example
# and 	Returns True if both statements are true	                x < 5 and  x < 10
# or	Returns True if one of the statements is true	            x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

num = 3
num1 = 5

num < num1 and num == num1 

num < num1 or num == num1

not(num < num1 and num == num1)

# IDENTITY OPERATORS

# Operator	Description	                                            Example
# is 	    Returns True if both variables are the same object	    x is y
# is not	Returns True if both variables are not the same object	x is not y

college_graduate_age is able_to_purchase_alcohol # True

# String and Numbers are straightforward but once we get into objects...

# IF/ELIF/ELSE STATEMENT

# Python supports the usual logical (operators) conditions from mathematics:

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

e = 200
f = 33

if e == f: # careful comparing equals
    print("e is equal to f")
elif e > f:
    print("e is greater than f")
else:
    print("e is less than f")

##### ****INDENTATION**** #####