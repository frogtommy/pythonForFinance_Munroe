## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW4_LOOPS_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##

# Q1 (1 point)
# Create a function, exampleOne, which takes one integer input parameter.
# Using a loop, populate an array with all values from 0 up to that integer.
# Example Input Parameter: 5
# Example Output: [0, 1, 2, 3, 4]
def exampleOne(paramInt):
    newArray = []
    for i in range(paramInt):
        newArray.append(i)
    return newArray
print(exampleOne(3))



# Q2 (1 point):
# Create a function, exampleTwo, which takes two integer input parameters.
# Using a loop, populate an array with all values from the first integer to the second integer.
# Example Input Parameter: 2, 5
# Example Output: [2, 3, 4]
def exampleTwo(paramOne,paramTwo):
    array = []
    for i in range(paramOne,paramTwo):
        array.append(i)
    return array
print(exampleTwo(5,9))
print(exampleTwo(100,106))


    

# Q3 (1 point):
# Create a function, exampleThree, which takes two integer input parameters.
# Using a loop, populate an array with all values from the first integer to the second integer, skipping every other number.
# Example Input Parameter: 2, 10
# Example Output: [2, 4, 6, 8]
def exampleThree(paramOne,paramTwo):
    array = []
    for i in range(paramOne,paramTwo,2): ##counting by '2'
        array.append(i)
    return array
print(exampleThree(2,10))
print(exampleThree(9,18))


# Q4 (2 points):
# Create a function, exampleFour, which takes an input array
# Using a loop, populate a new array with all values from the input array, starting at the 2nd element, multiplied by the previous element
# Example Input Parameter: [2,3,4,5]
# Example Output: [6,12,20]
def exampleFour(paramOne):
    array = []
    for i in range(1,len(paramOne)):
        array.append(paramOne[i]*paramOne[i-1])
    return array
print(exampleFour([2,3,4,5]))
print(exampleFour([5,10,15,20,25]))



# Q5 (2 points):
# Create a function, exampleFive, which takes an input array
# Using a loop, populate a new array with all values from the input array that are even (hint: % operator)
# Example Input Parameter: [2, 3, 4, 5]
# Example Output: [2, 4]
def exampleFive(paramA):
    array = []
    for element in paramA:
        if element % 2 == 0:
            array.append(element)
        if element % 2 == 1: continue
    return array
print(exampleFive([2,3,4,5]))
print(exampleFive([5,10,15,20]))


# Q6 (3 points):
# Create a function, exampleSix, which takes two input arrays
# If the two arrays are equal in length, populate a new array with all values from the first input array multiplied by the second 
# If the two arrays are not equal in length, return "!Array Mismatch!"
def exampleSix(paramOne,paramTwo):
    if len(paramOne) == len(paramTwo):
        array = []
        for i in range(len(paramOne)):
            array.append(paramOne[i] * paramTwo[i])
        return array
    else:
        return '!Array Mismatch!'
print(exampleSix([1,2,3,4,5], [6,7,8,9,10]))
print(exampleSix([-1,-2,-3,-4,-5], [-10,-9,-8,-7,-6]))
