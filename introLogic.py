
# A function which takes two input parameters.
# Returns True if these parameters are equal to each other
# Returns False if these parameters are not equal to each other
def exampleOne(paramOne, paramTwo):
    if( paramOne == paramTwo ):
        value = True
    else: value = False
    return value
print(exampleOne("GS","GS"))
print(exampleOne("GS","JPM"))






# A fucntion which takes three input parameters
# Returns True if none of these parameters all equal eachother
# Returns False if not
def exampleTwo(paramOne, paramTwo, paramThree):
    if( paramOne == paramTwo == paramThree):
        value = True
    else: value = False
    return value
print(exampleTwo("GS","GS","GS"))
print(exampleTwo("GS","GS","notGS"))



# A function which takes two input parameters: an array and an integer
# Returns True if the integer is greater than, or equal to, the length of the array
# Returns False if the array is smaller than the length of the array
def exampleThree(paramArray, paramInt):
    if( paramInt >= len(paramArray)):
        value = True
    else: value = False
    return value
print(exampleThree([1,2,3,4,5,6,7],5))
print(exampleThree([1,2,3],7))




# A function which takes three input parameters
# Returns True if either first is different from second or second is same as third
# Otherwise, returns False
def exampleFour(paramOne, paramTwo, paramThree):
    return not(paramOne == paramTwo) or paramTwo == paramThree
i1 = "Spring"
i2 = "Summer"
i3 = "Fall"
i4 = "Winter"
print(exampleFour(i1,i2,i3))
print(exampleFour(i1,i1,i2))
print(exampleFour(i1,i2,i2))





# S function which takes two input parameters
# Returns True if first param is part of second param
# Returns False if second param is part of first param
# Returns 0 otherwise
def exampleFive(paramOne,paramTwo):
    if paramOne in paramTwo:
        return True
    if paramTwo in paramOne:
        return False
    else: return 0
print(exampleFive("SaltLake", "Lake"))
print(exampleFive("Salt","Lake"))




# A function which takes three input parameters: 2 arrays, and 1 string
# Returns "Both" if the string is in both arrays
# Returns "First" if the string in only in the first array
# Returns "Second" if the string is only in the second array
# Returns "Neither" if the string is in neither arrays
def exampleSix(pOneArray, pTwoArray, pThreeStr):
    if(pThreeStr in pOneArray and pThreeStr in pTwoArray):
        return "Both"
    if pThreeStr in pOneArray:
        return "First"
    if pThreeStr in pTwoArray:
        return "Second"
    else: return "Neither"

testArray = ["Python", "Rules", "Data", "Science"]
testArray2 = ['STATA', "Rules", "Econometric"]
print(exampleSix(testArray,testArray2,"STATA"))
print(exampleSix(testArray,testArray2,"Rules"))
print(exampleSix(testArray,testArray2,"Python"))
print(exampleSix(testArray,testArray2,"nill"))