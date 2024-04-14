# Some notes about writing short code
# #########################################

# fmt: off

# #########################################
# instead of using input() function, we can use open() function to read the input from the file
# reads three lines from stdin.
a,b,c = open(0)


# #########################################
# reuse input for print
I=input
a=I()
b=I()
I(a + b)  # <-- prints with input. Valid as result on codingame

# #########################################
# input short form
I=input
a,b=I(),I()

# #########################################
# if else without those keywords. The list indexing evaluates to 0 or 1
print([n,"No codes"][n<3])

# #########################################
# Only need one space as indentation
if x<1:
 print("X")
 print("Y")

# #########################################
# No need for indentation if single function call
if x<1:print("X")
