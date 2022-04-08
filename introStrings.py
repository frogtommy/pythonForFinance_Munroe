def exampleOne():
    return "Lorem Ipsum!"
print(exampleOne())



def exampleTwo(paramOne):
    newString = "(" + paramOne + ")"
    return newString
print(exampleTwo("second one"))
print(exampleTwo("third one"))




def exampleThree(paramOne,paramTwo):
    operationResult = "This " + paramOne + " and that " + paramTwo
    return operationResult
print( exampleThree("Apple","Orange") )




def exampleFour(paramOne,paramTwo):
    return(paramOne.strip(paramTwo))
print(exampleFour("$$$$DOLLAR_SIGN$$$$","$"))



def exampleFive(paramOne):
    divideSeven = (float(paramOne))/7
    normalNum = float(paramOne)
    dogYears = "In dog years, I am {}. But, in humans years I am {}"
    # return dogYears
    return dogYears.format(str(divideSeven), str(normalNum))
print(exampleFive(49))
print(exampleFive("21"))



def exampleSix(paramOne):
    paramOne = paramOne.replace("a", "")
    paramOne = paramOne.replace("e", "")
    paramOne = paramOne.replace("i", "")
    paramOne = paramOne.replace("o", "")
    paramOne = paramOne.replace("u", "")
    return paramOne
print(exampleSix("university of utah"))



def example(paramOne):
    return paramOne.replace("aa", "a").replace("yy", "y")

print(example('aahoy laddyy'))


