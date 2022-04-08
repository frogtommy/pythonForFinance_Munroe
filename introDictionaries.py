
# A function which takes four input parameters, all of which are either strings or integers
# Makes and returns a dictionary from these four input parameters where the first two parameters are keys and the second two parameters are values

def exampleOne(paramOne,paramTwo,paramThree,paramFour):
    dict = {paramOne:paramTwo, paramThree:paramFour}
    return dict
print(exampleOne("key1","key2","value1","value2"))



# A function which takes one input parameters that is an array of arrays (embedded array). Each inner array has 2 elements
# Populates a dictionary where the first element of each inner array is a key and the second element of each inner array is a value

def exampleTwo(paramOne):
    dict = {}
    for array in paramOne:
        key = array[0]
        value = array[1]
        dict[key] = value
    return dict
print(exampleTwo([ ["key1","value1"],["key2","value2"]]))



# A function which takes two input parameters. A first parameter is a dictionary, the second parameter is a string
# Checks if the dictionary contains the string parameter as a key. If so, returns the associated value
# If the dictionary doesn't contain the key specified by the string, returns 0
def exampleThree(paramDict, paramStr):
    element = paramDict.get(paramStr,0)
    return element*element
print(exampleThree({"key1":200,"key2":30},"key2"))



# A function with two input parameters. The first input parameter is an array of letters. The second input parameter is an array of words
# Populates a dictionary that makes key-value pairs matching each letter with the first letter of each word

def exampleFour(paramLetter,paramWord):
    dict = {}
    for letter in paramLetter:
        for word in paramWord:
            if letter == word[0]:
                dict[letter] = word
    return dict
print(exampleFour(["K", "G","U"], ["Gosudarstvenniy", "Kazanski","Universitet"]))

