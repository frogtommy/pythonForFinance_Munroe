
#A function which has two input arrays. This returns the sum of the length of both arrays.

def exampleOne(param1,param2):
    doubleArray = param1 + param2
    return len(doubleArray)

testArray=[1,2,3,4,5,6,'q']
testArray2=[1,"duo",3,4]
print(exampleOne(testArray,testArray2))



# A function which has one input array. This returns the first element multiplied by the last element
def exampleTwo(param1):
    firstElem = param1[0]
    lastElem = param1[len(param1)-1]
    return firstElem*lastElem

testArray3 = [1, 2, 3, 4, 5]
testArray4 = [3, 2, 3, 4, 9]
print(exampleTwo(testArray3))
print(exampleTwo(testArray4))




# A function which takes three parameters that are string/integers. This returns an array that is the combination
# of these three elements (in the order they were introduced)

def exampleThree(param1,param2,param3):
    # makeArray = [param1,param2,param3]
    # return makeArray
    return [param1,param2,param3]
print(exampleThree('apple','orange',3))





# A function that will have three input parameters array, number, string.
# This removes an element from input array under the index indicated by second input parameter.
# Replace second element in the input array with string from third parameter
# Add the removed parameter to the end of the array

def exampleFour(pArray,pNum,pStr):
    var = pArray.pop(pNum)
    pArray[1] = pStr
    pArray.append(var)
    return pArray
print(exampleFour(['apples', 'oranges', 'bananas'], 1, 'strawberries'))
print(exampleFour(['marketing', 'finance', 'accounting', 'economics'], 2, 'QAMO'))





# A function that will have one input array.
# This finds the first element of the array and add it to the end of the array.

def exampleFive(pArray):
    pArray.append(pArray[0])
    return pArray
print( exampleFive([1, 2, 3, 4, 5, 6, 'q']) )
print( exampleFive(['a', 'b', 'c', 'd', 'e', 'f']) )





# A function that will have one input array and one singular int
# This isolates the array so that it is only the 2nd, 3rd and 4th elements. Next, add the singular int to the end of the array

def exampleSix(pArray,pInt):
    pArray = pArray[1:4]
    pArray.append(pInt)
    return pArray
print(exampleSix([1,2,3,4,5,6], 8))
print(exampleSix(['a','b','c','d','e'], 'f'))




