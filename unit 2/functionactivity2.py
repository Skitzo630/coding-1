
elias  richardson<erichardson624@boyslatin.net>
9:50 AM (0 minutes ago)
to me

# PROBLEM #1
# Create a function that will take in 2 inputs and
# compare them.
# your inputs should be numbers.
# The function should compare if the first input is
# if it is the less than the second input it
# should prtint true. id it is not, it should print false.

def compareVal():
    numA= input()
    numB= input()
    print(numA <= numB)

# PROBLEM
# Create a function that will compare if a student
# has made honor

# The student should be able to input 2 pieces of data
# the fist should be their grade and the second should 
# be the number of days they have beens absent.

# if the studetens grade is above a 90 and the number
# of absenses is less then 5, the problem should print
# true, otherwise it should print false.

def CompareStudentHonorRole():
    grade = input("enter grade:")
    absent = input("enter absenses:")
    print(grade > 90 and absent < 5)
